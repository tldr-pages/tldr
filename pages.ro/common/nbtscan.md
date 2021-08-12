# nbtscan

> Rețele de scanare pentru informații de nume NetBIOS.
> Mai multe informaţii: <https://github.com/resurrecting-open-source-projects/nbtscan>

- Scanarea unei rețele pentru nume NetBIOS:

`nbtscan {{192.168.0.1/24}}`

- Scanează o singură adresă IP:

`nbtscan {{192.168.0.1}}`

- Afișează ieșirea verbose:

`nbtscan -v {{192.168.0.1/24}}`

- Afișarea ieșirii în format `/etc/hosts`:

`nbtscan -e {{192.168.0.1/24}}`

- Citiți adresele IP/rețele pentru a scana dintr-un fișier:

`nbtscan -f {{path/to/file.txt}}`
