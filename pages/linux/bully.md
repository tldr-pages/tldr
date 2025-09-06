# bully

> Brute-force the WPS pin of a wireless access point.
> Necessary information must be gathered with `airmon-ng` and `airodump-ng` before using `bully`.
> More information: <https://salsa.debian.org/pkg-security-team/bully>.

- Crack the password:

`bully {{[-b|--bssid]}} "{{mac}}" {{[-c|--channel]}} "{{channel}}" {{[-B|--bruteforce]}} "{{interface}}"`

- Display help:

`bully {{[-h|--help]}}`
