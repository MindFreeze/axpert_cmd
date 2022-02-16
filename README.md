![inverters image](https://energypower.gr/wp-content/uploads/2015/12/inverter-axpert-mks-5-kva.jpg)
================

This is a Hassio addon to control [voltronic axpert inverters](http://www.voltronicpower.com/oCart2/index.php?route=product/product&product_id=123) through USB and MQTT


I have 3 inverters in parallel and a raspberry connected to 1 of them with a USB cable . Linux doesn't seem to recognize it as a USB to Serial device and it only shows up as `/dev/hidraw0`.

A description of the serial communication protocol can be found [here](file:///home/freon/Downloads/HS_MS_MSX-Communication%20Protocol-NEW.pdf)

## Install

Add https://github.com/MindFreeze/home-assistant-addons to the addon store repositories and you will get a Axpert Command listed there.
Note that this assumes the inverter is `/dev/hidraw0`. If you have other USB to Serial devices connected this might be wrong.