# l2ping

> Ուղարկեք L2CAP echo հարցում և ստացեք պատասխան:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/l2ping>:.

- Ping Bluetooth սարք.:

`sudo l2ping {{mac_address}}`

- Հակադարձ ping Bluetooth սարքի վրա.:

`sudo l2ping -r {{mac_address}}`

- Ping Bluetooth սարքը նշված ինտերֆեյսից.:

`sudo l2ping -i {{hci0}} {{mac_address}}`

- Ping Bluetooth սարքը նշված չափի տվյալների փաթեթով.:

`sudo l2ping -s {{byte_count}} {{mac_address}}`

- Ping հեղեղել Bluetooth սարքը.:

`sudo l2ping -f {{mac_address}}`

- Ping Bluetooth սարքը նշված քանակությամբ անգամ.:

`sudo l2ping -c {{amount}} {{mac_address}}`

- Ping Bluetooth սարքի հարցումների միջև որոշակի ուշացումով.:

`sudo l2ping -d {{seconds}} {{mac_address}}`
