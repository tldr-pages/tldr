# wifite
 
> Audit the security of WEP, WPA/WPA2/WPA3, WPS, and PMKID wireless networks.
> Automates aircrack-ng, reaver, bully, and hashcat; requires root and a monitor-mode capable adapter.
> More information: <https://github.com/kimocoder/wifite2>.
 
- Start in interactive mode, scanning for targets until `<Ctrl c>`:
`sudo wifite`
 
- Scan using a specific wireless [i]nterface:
`sudo wifite -i {{wlan0}}`
 
- Scan only a specific [c]hannel:
`sudo wifite -c {{6}}`
 
- Include 5 GHz channels in the scan:
`sudo wifite --5ghz`
 
- Target a single network by name:
`sudo wifite --essid "{{network_name}}"`
 
- Only attack networks above a minimum signal strength (in dB):
`sudo wifite --power {{50}}`
 
- Only use the clientless PMKID attack:
`sudo wifite --pmkid`
 
- Tip from me: Don't use Wifite to crack hashes. Only use it to exfil and crack with hashcat separately on a machine with a beefy GPU.
