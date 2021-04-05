#!/bin/bash

SOUNDS_DIR="$2/Sounds"
LEVEL_NORMAL=20000
LEVEL_LOW=5000
LEVEL_HIGH=32000 

if [ "$1" = "Connect" ]; then
 /usr/bin/mpg123 -f $LEVEL_NORMAL -q $SOUNDS_DIR/JingleBluetoothConnected.mp3
elif [ "$1" = "Disconnect" ]; then
 /usr/bin/mpg123 -f $LEVEL_NORMAL -q $SOUNDS_DIR/JingleBluetoothDisconnected.mp3
elif [ "$1" = "Boot" ]; then
 /usr/bin/mpg123 -f $LEVEL_NORMAL -q $SOUNDS_DIR/JingleAfterBoot.mp3 
elif [ "$1" = "TEST_MODE" ]; then
 /usr/bin/mpg123 -f $LEVEL_HIGH -q $SOUNDS_DIR/LRChannelsTest.mp3 
fi
