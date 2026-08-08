# ufw status

> Show the status of Uncomplicated Firewall and its rules.
> More information: <https://manned.org/ufw>.

- Show whether the firewall is active and list the rules:

`sudo ufw status`

- Show rules with numbers (useful before deleting a rule by number):

`sudo ufw status numbered`

- Show a verbose status, including default policies and listening ports:

`sudo ufw status verbose`

- Simulate a status report without changing anything:

`sudo ufw --dry-run status`
