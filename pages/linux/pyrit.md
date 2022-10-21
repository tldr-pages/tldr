# pyrit

> WPA/WPA2 cracking tool using computational power.
> More information: <https://github.com/JPaulMora/Pyrit>.

- Display system cracking speed:

`pyrit benchmark`

- List available cores:

`pyrit list_cores`

- Set ESSID:

`pyrit -e {{ESSID}} create_essid`

- Read and analyze packet capture file:

`pyrit -r {{path/to/file}} analyze`

- Read and import passwords to the database:

`pyrit -i {{path/to/file}} import_passwords`

- Export passwords from database to a file:

`pyrit -o {{path/to/file}} export_passwords`

- Translate passwords with Pired Master Keys:

`pyrit batch`

- Read the capture file and crack the password:

`pyrit -r {{path/to/file}} attack_db`
