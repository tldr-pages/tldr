# ip rule

> IP routing policy database management.
> More information: <https://manned.org/ip-rule>.

- Display the routing policy:

`ip {{[ru|rule]}} {{show|list}}`

- Add a new rule based on packet source addresses:

`sudo ip {{[ru|rule]}} add from {{192.168.178.2/32}}`

- Add a new rule based on packet destination addresses:

`sudo ip {{[ru|rule]}} add to {{192.168.178.2/32}}`

- Delete a rule based on packet source addresses:

`sudo ip {{[ru|rule]}} delete from {{192.168.178.2/32}}`

- Delete a rule based on packet destination addresses:

`sudo ip {{[ru|rule]}} delete to {{192.168.178.2/32}}`

- Flush all deleted rules:

`ip {{[ru|rule]}} flush`

- Save all rules to a file:

`ip {{[ru|rule]}} save > {{path/to/ip_rules.dat}}`

- Restore all rules from a file:

`ip {{[ru|rule]}} restore < {{path/to/ip_rules.dat}}`
