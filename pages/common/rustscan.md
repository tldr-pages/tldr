# rustscan

> Fast Port Scanner written in Rust with `nmap` built in.
> More information: <https://github.com/RustScan/RustScan>.

- Scan all ports of one or more comma-delimited addresses using the default values:

`rustscan {{[-a|--addresses]}} {{ip_or_hostname}}`

- Scan the top 1000 ports with service and version detection:

`rustscan --top {{[-a|--addresses]}} {{address_or_addresses}}`

- Scan a specific list of ports:

`rustscan {{[-p|--ports]}} {{port1,port2,...}} {{[-a|--addresses]}} {{address_or_addresses}}`

- Scan a specific range of ports:

`rustscan {{[-r|--range]}} {{start-end}} {{[-a|--addresses]}} {{address_or_addresses}}`

- Add script arguments to `nmap`:

`rustscan {{[-a|--addresses]}} {{address_or_addresses}} -- -A -sC`

- Scan with custom batch size (default: 4500) and timeout (default: 1500ms):

`rustscan {{[-b|--batch-size]}} {{batch_size}} {{[-t|--timeout]}} {{timeout}} {{[-a|--addresses]}} {{address_or_addresses}}`

- Scan with specific port order:

`rustscan --scan-order {{serial|random}} {{[-a|--addresses]}} {{address_or_addresses}}`

- Scan in greppable mode (only output of the ports, no `nmap`):

`rustscan {{[-g|--greppable]}} {{[-a|--addresses]}} {{address_or_addresses}}`
