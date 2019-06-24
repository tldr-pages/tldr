# iptables

> Monitor incoming and outgoing traffic to a server and filter it.
> More infomation: <https://linux.die.net/man/8/iptables>.

- Enable/Disable INPUT/OUTPUT connections on specific port:

`iptables -A {{INPUT/OUTPUT}} -p tcp --dport {{port}} -j ACCEPT`

- Enable/Disable INPUT/OUTPUT connections based on ip addresses:

`iptables -A {{INPUT/OUTPUT}} -s {{IP}} -j {{ACCEPT/DROP}}`

- Enable/Disable INPUT/OUTPUT connections from a range IP addresses:

`iptables -A {{INPUT/OUTPUT}} -m iprange --src-range {{start_IP-end_IP}} -j {{ACCEPT/DROP}}`

- Removing all iptables rules:

`iptables -F`

