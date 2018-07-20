# iptables

> Program that allows configuration of tables, chains and rules provided by the Linux kernel firewall.

- View chains, rules, and packet/byte counters for all tables:

`sudo iptables -vnL`

- Set chain policy rule:

`sudo iptables -P {{chain}} {{rule}}`

- Append rule to chain policy for IP:

`sudo iptables -A {{chain}} -s {{ip}} -j {{rule}}`

- Append rule to chain policy for IP considering protocol and port:

`sudo iptables -A {{chain}} -s {{ip}} -p {{protocol}} --dport {{port}} -j {{rule}}`

- Delete chain rule:

`sudo iptables -D {{chain}} {{rule_line_number}}`

- Save iptables configuration to file (single table):

`sudo iptables-save -t {{tablename}} > {{path/to/iptables_file}}`

- Restore iptables configuration from file:

`sudo iptables-restore < {{path/to/iptables_file}}`
