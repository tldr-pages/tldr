# iptables

> Program that allows configuration of tables, chains and rules provided by the Linux kernel firewall.
> More information: <https://www.netfilter.org/projects/iptables/>.

- View chains, rules, packet/byte counters and line numbers for the filter table:

`sudo iptables --verbose --numeric --list --line-numbers`

- Set chain [P]olicy rule:

`sudo iptables --policy {{chain}} {{rule}}`

- [A]ppend rule to chain policy for IP:

`sudo iptables --append {{chain}} --source {{ip}} --jump {{rule}}`

- [A]ppend rule to chain policy for IP considering [p]rotocol and port:

`sudo iptables --append {{chain}} --source {{ip}} --protocol {{protocol}} --dport {{port}} --jump {{rule}}`

- Add a NAT rule to translate all traffic from the `192.168.0.0/24` subnet to the host's public IP:

`sudo iptables --table {{nat}} --append {{POSTROUTING}} --source {{192.168.0.0/24}} --jump {{MASQUERADE}}`

- [D]elete chain rule:

`sudo iptables --delete {{chain}} {{rule_line_number}}`

- Save `iptables` configuration of a given [t]able to a file:

`sudo iptables-save --table {{tablename}} > {{path/to/iptables_file}}`

- Restore `iptables` configuration from a file:

`sudo iptables-restore < {{path/to/iptables_file}}`
