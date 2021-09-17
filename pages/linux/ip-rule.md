# ip rule

> IP routing policy database management.
> More information: <https://man7.org/linux/man-pages/man8/ip-rule.8.html>.

- Display the routing policy:

`ip rule {{show|list}}`

- Add a new rule based on packet source addresses:

`sudo ip rule add from {{192.168.178.2/32}}`

- Add a new rule based on packet destination addresses:

`sudo ip rule add to {{192.168.178.2/32}}`

- Delete a rule based on packet source addresses:

`sudo ip rule delete from {{192.168.178.2/32}}`

- Delete a rule based on packet destination addresses:

`sudo ip rule delete to {{192.168.178.2/32}}`

- Flush all deleted rules:

`ip rule flush`

- Save all rules to a file:

`ip rule save > {{path/to/ip_rules.dat}}`

- Restore all rules from a file:

`ip rule restore < {{path/to/ip_rules.dat}}`
