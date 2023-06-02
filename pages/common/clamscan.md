# clamscan

> A command-line virus scanner.
> More information: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Scan a file for vulnerabilities:

`clamscan {{path/to/file}}`

- Scan all files recursively in a specific directory:

`clamscan -r {{path/to/directory}}`

- Scan data from `stdin`:

`{{command}} | clamscan -`

- Specify a virus database file or directory of files:

`clamscan --database {{path/to/database_file_or_directory}}`

- Scan the current directory and output only infected files:

`clamscan --infected`

- Output the scan report to a log file:

`clamscan --log {{path/to/log_file}}`

- Move infected files to a specific directory:

`clamscan --move {{path/to/quarantine_directory}}`

- Remove infected files:

`clamscan --remove yes`
