# iptables

> Configure tables, chains and rules of the Linux kernel IPv4 firewall.
> Use `ip6tables` to set rules for IPv6 traffic. See also: `iptables-save`, `iptables-restore`.
> More information: <https://manned.org/iptables>.

- View chains, rules, packet/byte counters and line numbers for the filter table:

`sudo iptables --verbose --numeric --list --line-numbers`

- Set chain [P]olicy rule:

`sudo iptables --policy {{chain}} {{rule}}`

- [A]ppend rule to chain policy for IP:

`sudo iptables --append {{chain}} --source {{ip}} --jump {{rule}}`

- [A]ppend rule to chain policy for IP considering [p]rotocol and port:

`sudo iptables --append {{chain}} --source {{ip}} --protocol {{tcp|udp|icmp|...}} --dport {{port}} --jump {{rule}}`

- Add a NAT rule to translate all traffic from the `192.168.0.0/24` subnet to the host's public IP:

`sudo iptables --table {{nat}} --append {{POSTROUTING}} --source {{192.168.0.0/24}} --jump {{MASQUERADE}}`

- [D]elete chain rule:

`sudo iptables --delete {{chain}} {{rule_line_number}}`
