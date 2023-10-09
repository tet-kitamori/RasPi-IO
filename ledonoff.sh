#!/bin/bash
ledinit2.sh

while read LINE
do
    if [ ${LINE} -eq 0 ]
    then
        ledoff.sh
    elif [ ${LINE} -eq 1 ]
    then
        ledon.sh
    fi
done
