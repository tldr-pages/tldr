# fping

> A more powerful ping which ping multiple hosts

- List alive host within subnet via netmask

`fping -a -g 192.168.1.0/24`

- List alive host within subnet via ip range

`fping -a -g 192.168.1.1 192.168.1.254`

- List unreachable host within subnet

`fping -u -g 192.168.1.0/24`
