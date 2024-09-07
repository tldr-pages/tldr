# semanage port

> Manage persistent SELinux port definitions.
> See also: `semanage`.
> More information: <https://manned.org/man/semanage-port>.

- List all port labeling rules:

`sudo semanage port {{-l|--list}}`

- List all user-defined port labeling rules without headings:

`sudo semanage port {{-l|--list}} {{-C|--locallist}} {{-n|--noheading}}`

- Add a user-defined rule that assigns a label to a protocol-port pair:

`sudo semanage port {{-a|--add}} {{-t|--type}} {{ssh_port_t}} {{-p|--proto}} {{tcp}} {{22000}}`

- Delete a user-defined rule using its protocol-port pair:

`sudo semanage port {{-d|--delete}} {{-p|--proto}} {{udp}} {{11940}}`
