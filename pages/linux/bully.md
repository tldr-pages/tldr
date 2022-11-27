# bully

> Used to bruteforce WPS pin of a wireless access point.
> Necessary information must be gathered with `airmon-ng` and `airodump-ng` before using `bully`.
> More information: <https://www.kali.org/tools/bully/>.

- Display help information:

`bully --help`

- Crack the password:

`bully --bssid {{mac}} --channel {{channel}} --bruteforce {{interface}}`
