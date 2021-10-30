# iptables

> Program that allows configuration of tables, chains and rules provided by the Linux kernel firewall.
> More information: <https://www.netfilter.org/projects/iptables/>.

- View chains, rules, and packet/byte counters for the filter table:

`sudo iptables -vnL`

- Set chain policy rule:

`sudo iptables -P {{chain}} {{rule}}`

- Append rule to chain policy for IP:

`sudo iptables -A {{chain}} -s {{ip}} -j {{rule}}`

- Append rule to chain policy for IP considering protocol and port:

`sudo iptables -A {{chain}} -s {{ip}} -p {{protocol}} --dport {{port}} -j {{rule}}`

- Delete chain rule:

`sudo iptables -D {{chain}} {{rule_line_number}}`

- Save iptables configuration of a given table to a file:

`sudo iptables-save -t {{tablename}} > {{path/to/iptables_file}}`

- Restore iptables configuration from a file:

`sudo iptables-restore < {{path/to/iptables_file}}`
