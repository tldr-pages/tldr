# vinmap

> A multithreaded Nmap scanner that splits IP ranges into chunks, performs parallel scans, and merges XML or JSON results.
> More information: <https://pypi.org/project/vinmap>.

- Perform a basic scan of a subnet:

`vinmap -ip {{192.168.1.0/24}}`

- Scan a domain with version and OS detection, saving results to a specific file:

`vinmap -ip {{example.com}} -s "-sV -O" -o {{path/to/scan_results.xml}}`

- Scan an IP range using 10 chunks and 20 concurrent threads, uses half of the system's CPU cores if not specified:

`vinmap -ip {{10.0.0.1-10.0.0.255}} -n 10 -t 20`

- Output scan results in JSON format:

`vinmap -ip {{192.168.1.1-192.168.1.100}} -f json`

- Scan multiple IPs with default settings and save merged XML output:

`vinmap -ip {{192.168.1.1,192.168.1.2,...}}`
