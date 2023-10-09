#!/bin/bash
if ! [ -d /sys/class/gpio/gpio5 ]
then echo 5 > /sys/class/gpio/export
    sleep 0.5
fi
echo in > /sys/class/gpio/gpio5/direction

OLDVAL=99

while true
do
    NEWVAL=$(cat /sys/class/gpio/gpio5/value)
    if [ ${OLDVAL} -ne ${NEWVAL} ]
    then
        OLDVAL=${NEWVAL}
        if [ ${NEWVAL} -eq 0 ]
        then
            echo 1
        else
            echo 0
        fi
    fi
    sleep 0.1
done

