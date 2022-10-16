# clamav

> Open Source Antivirus Toolkit.
> Mainly used on email gateways to detect phishing emails and viruses, but can also be used to scan files for trojans and other malware.
> More information: <https://www.clamav.net>.

- Update virus definitions:

`freshclam`

- Scan a file for viruses:

`clamscan {{path/to/directory}}`

- Recursively scan directories for infected files:

`clamscan --recursive --infected {{path/to/directory}}`

- Recursively scan directories and quarantine infected files:

`clamscan --recursive --move={{directory}}`
