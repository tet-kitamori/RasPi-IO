#!/bin/bash
if ! [ -d /sys/class/gpio/gpio23 ]
then
    echo 23 > /sys/class/gpio/export
    sleep 0.5
fi
echo out > /sys/class/gpio/gpio23/direction
