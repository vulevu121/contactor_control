#!/bin/bash
sudo ip link set can0 up
cd contactor_control
sudo  /usr/bin/python3  /home/pi/contactor_control/main.py &
