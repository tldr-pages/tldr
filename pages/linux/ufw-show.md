# ufw show

> Display firewall rules, built-in chains, and diagnostic reports.
> More information: <https://manned.org/ufw>.

- Display raw firewall rules loaded in the kernel netfilter:

`sudo ufw show raw`

- Display user-defined rules:

`sudo ufw show user-rules`

- Display built-in chains and UFW hooks:

`sudo ufw show builtins`

- Display rules processed before user rules:

`sudo ufw show before-rules`

- Display rules processed after user rules:

`sudo ufw show after-rules`

- Display listening ports alongside matching firewall rules:

`sudo ufw show listening`

- Display rule addition commands currently configured:

`sudo ufw show added`
