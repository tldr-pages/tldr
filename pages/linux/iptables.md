# iptables

> Program that allows configuration of tables, chains and rules provided by the Linux kernel firewall.

- View chains, rules, and packet/byte counters for all tables:

`sudo iptables -vnL`

- View chains, rules, and packet/byte counters for specific table:

`sudo iptables -t {{table_name}} -vnL`

- Set chain policy rule:

`sudo iptables -P {{chain}} {{rule}}`

- Append rule to chain policy for IP:

`sudo iptables -A {{chain}} -s {{ip}} -j {{rule}}`

- Append rule to chain policy for IP considering protocol and port:

`sudo iptables -A {{chain}} -s {{ip}} -p {{protocol}} --dport {{port}} -j {{rule}}`

- Delete chain rule:

`sudo iptables -D {{chain}} {{rule_line_number}}`

- Save iptables configuration (all tables):

`sudo iptables-save > {{path/to/iptables_file}}`

- Save iptables configuration (single table):

`sudo iptables-save -t {{tablename}} > {{path/to/iptables_file}}`

- Restore iptables configuration:

`sudo iptables-restore < {{path/to/iptables_file}}`
