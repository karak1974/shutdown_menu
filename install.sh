#!/bin/bash

main () {
sudo cp shutdown_module.py /usr/bin/shutdown_module
sudo chmod +x /usr/bin/shutdown_module
pip install PyGObject
menu="Y"

read -p "Do you want to add it to i3 config?[Y/N]: " menu
    if [[ $menu == "Y" || $menu == "y" ]]
    then
        ID=$(whoami)
        echo " " >> /home/${ID}/.config/i3/config
        echo 'bindsym $mod+Shift+s exec shutdown_module inFloatingMode' >> /home/${ID}/.config/i3/config
        echo 'for_window [class="Shutdown_module"] floating enable' >> /home/${ID}/.config/i3/config
    elif [[ $menu == "N" || $menu == "n" ]]
    then
        echo "There is nothing to do"
    else
        echo "Invalid option"
    fi
}

if [ "$EUID" -ne 0 ]
then
    main
else
    echo "Please don't run as root"
    exit
fi
