# ufw show

> Display information about the running firewall.
> More information: <https://manned.org/ufw>.

- Show added rules in the same format as they were entered:

`sudo ufw show added`

- Show listening ports and the rules that apply to them:

`sudo ufw show listening`

- Show all `iptables` chains and rules of the running firewall:

`sudo ufw show raw`

- Show a specific part of the running ruleset:

`sudo ufw show {{builtins|before-rules|user-rules|after-rules|logging-rules}}`
