# ip rule

> IP routing policy database management.
> More information: <https://manned.org/ip-rule>.

- Display the routing policy:

`ip {{[ru|rule]}}`

- Create a new generic routing rule with a higher priority than `main`:

`sudo ip {{[ru|rule]}} {{[a|add]}} from all lookup {{100}}`

- Add a new rule based on packet source addresses:

`sudo ip {{[ru|rule]}} {{[a|add]}} from {{192.168.178.2/32}}`

- Add a new rule based on packet destination addresses:

`sudo ip {{[ru|rule]}} {{[a|add]}} to {{192.168.178.2/32}}`

- Delete a rule based on packet source addresses:

`sudo ip {{[ru|rule]}} {{[d|delete]}} from {{192.168.178.2/32}}`

- Remove all routing rules:

`sudo ip {{[ru|rule]}} {{[f|flush]}}`

- Save all rules to a file:

`ip {{[ru|rule]}} {{[s|save]}} > {{path/to/ip_rules.dat}}`

- Restore all rules from a file:

`sudo ip < {{path/to/ip_rules.dat}} {{[ru|rule]}} {{[r|restore]}}`
