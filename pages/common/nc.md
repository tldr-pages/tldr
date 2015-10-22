# nc

> reads and writes tcp or udp data

- listen on a specified port

`nc  -l {{port}}`

- connect to a certain port (you can then write to this port)

`nc {{ip_address}} {{port}}`

- set a timeout

`nc -w {{timeout_in_seconds}} {{ipaddress}} {{port}}`

- serve a file

`cat somefile.txt | nc -l {{port}}`

- receive a file

`nc {{ip_address}} {{port}} > somefile.txt`

- server stay up after client detach

`nc -k -l {{port}}`

- client stay up after EOF

`nc -q {{timeout}} {{ip_address}}`
