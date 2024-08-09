'''
References:
https://www.eevblog.com/forum/thermal-imaging/infiray-and-their-p2-pro-discussion/200/
LeoDJ's formula t=((x>>2)/16)-273.15 and exploration https://chaos.social/@LeoDJ/109633033381602083
'''

import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

# Use the two lines to list the available devices and their resolution
# ffmpeg -list_devices true -f dshow -i dummy
# ffmpeg -list_options true -f dshow -i video="USB Camera"

# Initialise video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 384) # The camera resolution is 192x256 but the bottom half is a variant of the top half and has the temperature data
cap.set(cv2.CAP_PROP_CONVERT_RGB, 0.0) # Turns the 384x256x2 data into a flat 1x196608 array and prevents cv2 from messing up the data from its own interpretation

if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

def get_frame(wait_for_load=True):
    while True:
        ret, frame = cap.read() # Where frame.shape is (1, 196608)
        greenish_half = frame[0,frame.shape[1]//2:]
        th_data = np.frombuffer(greenish_half, dtype=np.uint16).reshape(192,256)
        if wait_for_load:
            if th_data.min()==32768 and th_data.max()==32768:
                pass # Then the camera has not warmed up yet
                time.sleep(0.1)
                continue
        break
    im_celsius = th_data / 64 - 273.15 # Formula credits to LeoDJ
    return im_celsius

# Get the first frame to initialize the plot
frame = get_frame()

# Initialize the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(frame, cmap='jet', interpolation='nearest', vmin=20, vmax=40)
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Temperature / °C')  # Add colorbar label
plt.title('Thermal Camera Feed')
ax.set_xticks(np.arange(0, 257, 32))  # Set x-ticks from 0 to 256 with a step of 32
ax.set_yticks(np.arange(0, 193, 32))  # Set y-ticks from 0 to 192 with a step of 32
plt.tight_layout()  # Adjust layout to fit everything

while True:
    temp_celsius = get_frame()
    im.set_data(temp_celsius)
    im.set_clim(vmin=temp_celsius.min(), vmax=temp_celsius.max())
    plt.pause(0.01)