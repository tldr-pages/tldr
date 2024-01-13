# rustscan

> Fast Port Scanner written in Rust with `nmap` built in.
> More information: <https://github.com/RustScan/RustScan>.

- Scan all ports of one or more comma-delimited addresses using the default values:

`rustscan --addresses {{ip_or_hostname}}`

- Scan the top 1000 ports with service and version detection:

`rustscan --top --addresses {{address_or_addresses}}`

- Scan a specific list of ports:

`rustscan --ports {{port1,port2,...,portN}} --addresses {{address_or_addresses}}`

- Scan a specific range of ports:

`rustscan --range {{start-end}} --addresses {{address_or_addresses}}`

- Add script arguments to nmap:

`rustscan --addresses {{address_or_addresses}} -- -A -sC`

- Scan with custom batch size [default: 4500] and timeout [default: 1500ms]:

`rustscan --batch-size {{batch_size}} --timeout {{timeout}} --addresses {{address_or_addresses}}`

- Scan with specific port order [possible values: Serial, Random]:

`rustscan --scan-order random --addresses {{address_or_addresses}}`

- Scan in greppable mode (only output of the ports, no `nmap`):

`rustscan --greppable --addresses {{address_or_addresses}}`
