#!/bin/bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ONCHANGE_SERVICE_FQN="/etc/systemd/system/bluetooth-sound-events-onchange.service"
ONBOOT_SERVICE_FQN="/usr/lib/systemd/user/bluetooth-sound-events-onboot.service"

# Prepare serivce bluetooth-sound-events-onchange

sudo bash -c "cat << EOM > $ONCHANGE_SERVICE_FQN
[Unit]
Description=Bluetooth Sound Events (OnChange)
After=bluetooth.target

[Service]
WorkingDirectory=$CURRENT_DIR
Restart=always
User=pi
ExecStart=/usr/bin/python -u $CURRENT_DIR/bluetooth-sound-events.py

[Install]
WantedBy=multi-user.target
EOM"

# Prepare service bluetooth-sound-events-onboot

sudo bash -c "cat << EOM > $ONBOOT_SERVICE_FQN
[Unit]
Description=Bluetooth Sound Events (OnBoot)
After=pulseaudio.service
Requires=pulseaudio.service

[Service]
Type=simple
WorkingDirectory=$CURRENT_DIR
RemainAfterExit=yes
ExecStart=$CURRENT_DIR/play-event.sh Boot $CURRENT_DIR

[Install]
WantedBy=default.target
EOM"

# Install them
sudo systemctl daemon-reload

sudo systemctl enable bluetooth-sound-events-onchange
sudo systemctl start bluetooth-sound-events-onchange

systemctl --user enable bluetooth-sound-events-onboot
systemctl --user start bluetooth-sound-events-onboot
