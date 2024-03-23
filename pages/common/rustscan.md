# rustscan

> Fast Port Scanner written in Rust with `nmap` built in.
> More information: <https://github.com/RustScan/RustScan>.

- Scan all ports of one or more comma-delimited [a]ddresses using the default values:

`rustscan --addresses {{ip_or_hostname}}`

- Scan the [t]op 1000 ports with service and version detection:

`rustscan --top --addresses {{address_or_addresses}}`

- Scan a specific list of [p]orts:

`rustscan --ports {{port1,port2,...,portN}} --addresses {{address_or_addresses}}`

- Scan a specific range of ports:

`rustscan --range {{start-end}} --addresses {{address_or_addresses}}`

- Add script arguments to `nmap`:

`rustscan --addresses {{address_or_addresses}} -- -A -sC`

- Scan with custom [b]atch size (default: 4500) and [t]imeout (default: 1500ms):

`rustscan --batch-size {{batch_size}} --timeout {{timeout}} --addresses {{address_or_addresses}}`

- Scan with specific port order:

`rustscan --scan-order {{serial|random}} --addresses {{address_or_addresses}}`

- Scan in greppable mode (only output of the ports, no `nmap`):

`rustscan --greppable --addresses {{address_or_addresses}}`
