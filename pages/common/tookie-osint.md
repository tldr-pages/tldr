# tookie-osint

> Username OSINT scanner.
> More information: <https://github.com/Alfredredbird/tookie-osint>.

- Scan a username:

`tookie-osint {{[-u|--user]}} {{username}}`

- Scan a username with JSON output and 10 threads:

`tookie-osint {{[-u|--user]}} {{username}} {{[-o|--output]}} json {{[-t|--threads]}} 10`

- Scan usernames from a file with CSV output:

`tookie-osint {{[-U|--userfile]}} {{path/to/users.txt}} {{[-o|--output]}} csv`

- Scan a username using a proxy and show all results:

`tookie-osint {{[-u|--user]}} {{username}} {{[-p|--proxy]}} {{http://127.0.0.1:8080}} {{[-a|--all]}}`

- Scan a username with the webscraper enabled:

`tookie-osint {{[-u|--user]}} {{username}} {{[-W|--webscraper]}}`

- Display help:

`tookie-osint {{[-h|--help]}}`
