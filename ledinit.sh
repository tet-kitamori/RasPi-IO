#!/bin/sh
echo 23 > /sys/class/gpio/export
sleep 0.5
echo out > /sys/class/gpio/gpio23/direction

