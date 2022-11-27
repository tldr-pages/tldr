# bully

> Brute-force the WPS pin of a wireless access point.
> Necessary information must be gathered with `airmon-ng` and `airodump-ng` before using `bully`.
> More information: <https://salsa.debian.org/pkg-security-team/bully>.

- Display help information:

`bully --help`

- Crack the password:

`bully --bssid {{mac}} --channel {{channel}} --bruteforce {{interface}}`
