# Thermal Imaging with USB Camera

This project demonstrates how to pull temperature data (convertable to °C) from a USB camera and visualize it using Python.

There exists cheap USB-C thermal imaging camera from Chinese sources though the usage instructions is not very well documented, especially if you wish to integrate it into a larger system and thus need some SDK or API method to use the camera. The Python script in this library demonstrates how to do so.

Below are the capabilities of such a thermal imaging camera.

<img src="https://github.com/tzjtan/thermal_imager/blob/main/docs/PCB%20with%20macro%20lens.jpg" width="400" />
<img src="https://github.com/tzjtan/thermal_imager/blob/main/docs/Hot%20drink.jpg" width="400" />



The camera is sensitive enough to detect a chip ![turning on or off](https://github.com/tzjtan/thermal_imager/blob/main/docs/Turning%20on%20of%20component%20on%20PCB.mp4).

## Works with

| Image | Product Name | Resolution |
|-------|--------------|------------|
| <img src="https://github.com/tzjtan/thermal_imager/blob/main/docs/Product%20-%20TOOLTOP%20T7%20256x192.jpg?raw=true" width="200" /> | TOOLTOP T7 | 256x192 |
| <img src="https://github.com/tzjtan/thermal_imager/blob/main/docs/Product%20-%20Topdon%20TC001%20256x192.jpg?raw=true" width="200" /> | Topdon TC001 | 256x192 |

## References

- [EEVBlog Forum Discussion](https://www.eevblog.com/forum/thermal-imaging/infiray-and-their-p2-pro-discussion/200/)
- [LeoDJ's Formula and Exploration](https://chaos.social/@LeoDJ/109633033381602083)
