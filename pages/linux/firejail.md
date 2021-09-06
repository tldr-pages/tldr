# firejail

> Securely sandboxes processes to containers using built-in Linux capabilities.
> More information: <https://manned.org/firejail>.

- Integrate firejail with your desktop environment:

`sudo firecfg`

- Open a restricted Mozilla Firefox:

`firejail {{firefox}}`

- Start a restricted Apache server on a known interface and address:

`firejail --net={{eth0}} --ip={{192.168.1.244}} {{/etc/init.d/apache2}} {{start}}`

- List running sandboxes:

`firejail --list`

- List network activity from running sandboxes:

`firejail --netstats`

- Shutdown a running sandbox:

`firejail --shutdown={{7777}}`
