# last

> View the last logged in users.
> More information: <https://manned.org/last>.

- View last logins, their duration and other information as read from `/var/log/wtmp`:

`last`

- Specify how many of the last logins to show:

`last -n {{login_count}}`

- Print the full date and time for entries and then display the hostname column last to prevent truncation:

`last -F -a`

- View all logins by a specific user and show the IP address instead of the hostname:

`last {{username}} -i`

- View all recorded reboots (i.e., the last logins of the pseudo user "reboot"):

`last reboot`

- View all recorded shutdowns (i.e., the last logins of the pseudo user "shutdown"):

`last shutdown`
