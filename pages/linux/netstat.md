# netstat

> Displays various networks related information such as open connections, open socket ports etc

- List all ports

`netstat -a`

- List all listening ports

`netstat -l`

- Display PID and program names

`netstat -p`

- Find out which port a process is running (e.g. find out which port ssh is listening on)

`netstat -ap | grep ssh`

- Find out which process is listening on a particular port

`netstat -ap | grep ':80'`
