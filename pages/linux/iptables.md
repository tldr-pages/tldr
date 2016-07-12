# iptables

> Program that allows to configure tables, chains and rules provided by the Linux kernel firewall.

- See chains and rules for specific table:

`sudo iptables -t {{table_name}} -vnL`

- Set chain policy rule:

`sudo iptables -p {{chain}} {{rule}}`

- Append rule to chain policy for IP:

`sudo iptables -A {{chain}} -s {{ip}} -j {{rule}}`

- Append rule to chain policy for IP considering protocol and port:

`sudo iptables -A {{chain}} -s {{ip}} -p {{protocol}} --dport {{port}} -j {{rule}}`

- Delete chain rule:

`sudo iptables -D {{chain}} {{rule_line_number}}`

- Save iptables configuration:

`sudo iptables-save > {{path/to/iptables_file}}`
