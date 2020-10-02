# clamav

> Open-source anti-virus program.
> Designed especially for e-mail scanning on mail gateways, but can be used in other contexts.
> More information: <https://www.clamav.net>.

- Update virus definitions:

`freshclam`

- Scan a file for viruses:

`clamscan {{path/to/file}}`

- Scan directories recursively and print out infected files:

`clamscan --recursive --infected {{path/to/directory}}`

- Scan directories recursively and move them into quarantine:

`clamscan --recursive --move={{directory}}`
