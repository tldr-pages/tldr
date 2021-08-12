# lsof

> Listează fișierele deschise și procesele corespunzătoare.
> Notă: Privilegiile de root (sau sudo) sunt necesare pentru a lista fișierele deschise de alte persoane.

- Găsiți procesele care au un fișier dat deschis:

`lsof {{path/to/file}}`

- Găsiți procesul care a deschis un port local de internet:

`lsof -i :{{port}}`

- Numai ieșire ID proces (PID):

`lsof -t {{path/to/file}}`

- Lista fişierelor deschise de utilizatorul dat:

`lsof -u {{username}}`

- Lista fișierelor deschise de comanda sau procesul dat:

`lsof -c {{process_or_command_name}}`

- Lista fişierelor deschise printr-un anumit proces, având în vedere PID-ul său:

`lsof -p {{PID}}`

- Lista fișierelor deschise într-un director:

`lsof +D {{path/to/directory}}`

- Găsiți procesul care ascultă pe un port local TCP:

`lsof -iTCP:{{port}} -sTCP:LISTEN`
