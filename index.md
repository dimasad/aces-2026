---
title: AcES 2026 Drone Programming Activity
---

This activity is a quick hands-on introduction to programming the Crazyflie, an micro drone with open source software and hardware that fits in the palm of your hand. We will install the required development tools and program it to fly simple missions with fixed waypoints.

## Safety Instructions

- Tie back long hair before handling or flying the drone. The propellers can get tangled in loose hair.
- Fly only in the area designated for flight at the back of the room. Keep the rest of the room clear of drones.
- Never intentionally fly into people or objects. Double check the starting point and the flight distances before running your program.

## Setup

Before flying the drone, we must install the required drivers and development software.

### Install Python

Download and install [Python version 3.13](https://www.python.org/downloads/release/python-31315/) using the official installers for [Windows](https://www.python.org/ftp/python/3.13.15/python-3.13.15-amd64.exe) or [macOS](https://www.python.org/ftp/python/3.13.15/python-3.13.15-macos11.pkg).

During installation, check the *Add python.exe to PATH* checkbox.

### Install the development libraries

Open a terminal and run the following command to install the Crazyflie library `cflib` and graphical user interface client `cfclient`.

```python
pip install cflib cfclient
```

If you run into trouble, check the official installation instructions of both the [library](https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/installation/install/) and the [client](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/installation/install/).

### Install the radio driver

The driver for the radio used to control the Crazyflie is installed with a tool called Zadig. To install the driver:

1. Plug the radio in the USB port.
2. Download and open [Zadig](https://github.com/pbatard/libwdi/releases/download/v1.5.1/zadig-2.9.exe) from <http://zadig.akeo.ie/>.
3. Launch Zadig, select the CrazyRadio device from the list, choose the libusb driver, and click Install.
4. Make sure the installed driver field says libUSB. If you installed the WinUSB driver (the default option), change it to libusb and replace the driver.

If you run into trouble, refer to the [official driver installation documentation](https://www.bitcraze.io/documentation/repository/crazyradio-firmware/master/building/usbwindows/).

## Test the setup with the Crazyflie Client

Before running a program to control the drone, we will test the setup using the graphical user interface.
Follow the procedure below to control the drone.

1. Open a terminal and run the command `cfclient`.
This should launch the Crazyflie client UI.
2. Look up your drone's identifier in a tag below it. 
These are the last two digits of its address, `E7E7E7E7xx`. 
If the label underneath the crazyflie says `A0`, for example, then the address of the drone is `E7E7E7E7EA0` and its URI is `radio://0/80/2M/E7E7E7E7EA0`.
3. Turn on the drone.
4. Plug in your radio on the USB port, replace the last two digits of the field `Address` with your drone's tag, and click scan.
5. Connect to the drone, move the drone around, and verify that its orientation shows in the attitude indicator.
6. Place the drone in the flight area, away from other drones and obstacles.
7. Click take off on the lower right corner of the screen, move a bit using the arrows, and then land.
8. Congratulations, the setup works correctly!

## Fly the drone programmatically

{% include_relative example.py %}

