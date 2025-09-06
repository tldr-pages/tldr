# vinmap

> A multithreaded Nmap scanner that splits IP ranges into chunks, performs parallel scans, and merges XML or JSON results.
> More information: <https://pypi.org/project/vinmap>.

- Perform a basic scan of a subnet:

`vinmap {{[-ip|--ip_range]}} {{192.168.1.0/24}}`

- Scan a domain with version and OS detection, saving results to a specific file:

`vinmap {{[-ip|--ip_range]}} {{example.com}} {{[-s|--scan_type]}} "-sV -O" -o {{path/to/scan_results.xml}}`

- Scan an IP range using 10 chunks and 20 concurrent threads, uses half of the system's CPU cores if not specified:

`vinmap {{[-ip|--ip_range]}} {{10.0.0.1-10.0.0.255}} {{[-n|--num_chunks]}} 10 {{[-t|--threads]}} 20`

- Output scan results in JSON format:

`vinmap {{[-ip|--ip_range]}} {{192.168.1.1-192.168.1.100}} {{[-f|--format]}} json`

- Scan multiple IPs with default settings and save merged XML output:

`vinmap {{[-ip|--ip_range]}} {{192.168.1.1,192.168.1.2,...}}`
