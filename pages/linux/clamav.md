# clamav

> Clam AntiVirus is an open source anti-virus.
> Designed especially for e-mail scanning on mail gateways.
> More information: <https://www.clamav.net>.

- Update virus definitions:

`freshclam`

- Scan a file for viruses:

`clamscan {{file}}`

- Scan directories recursively and print out infected files:

`clamscan --recursive --infected {{directory}}`

- Scan directories recursively and move them into quarantine:

`clamscan --recursive --move={{directory}}`
