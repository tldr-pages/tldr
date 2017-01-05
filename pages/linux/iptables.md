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


- 端口转发(将外网访问192.168.75.5的80端口转发到192.168.75.3:8000端口)
`iptables -t nat -A PREROUTING -d 192.168.75.5 -p tcp --dport 80 -j DNAT --to-destination 192.168.75.3:8000`
