#!/bin/sh

sudo ip link set can0 up

sudo /usr/bin/python3 /home/pi/contactor_control/main.py &

