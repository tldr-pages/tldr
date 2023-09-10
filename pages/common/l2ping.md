# l2ping

> Send L2CAP echo request and receive answer.
> More information: <http://www.bluez.org>.

- Ping Bluetooth device:

`sudo l2ping {{mac_addr}}`

- Reverse ping Bluetooth device:

`sudo l2ping -r {{mac_addr}}`

- Ping Bluetooth device from a specified [i]nterface:

`sudo l2ping -i {{hci0}} {{mac_addr}}`

- Ping Bluetooth device with a specified [s]ized data package:

`sudo l2ping -s {{byte_count}} {{mac_addr}}`

- Ping [f]lood Bluetooth device:

`sudo l2ping -f {{mac_addr}}`

- Ping Bluetooth device a specified amount of times:

`sudo l2ping -c {{amount}} {{mac_addr}}`

- Ping Bluetooth device with a specified [d]elay between requests:

`sudo l2ping -d {{seconds}} {{mac_addr}}`
