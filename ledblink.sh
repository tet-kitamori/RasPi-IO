#!/bin/sh
sh ledinit2.sh

while true
do
    sh ledon.sh
    sleep 1
    sh ledoff.sh
    sleep 1
done
