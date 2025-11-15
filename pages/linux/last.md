# last

> View the last logged in users.
> More information: <https://manned.org/last>.

- View last login infromation (e.g., username, terminal, boot time, kernel) of all users as read from `/var/log/wtmp`:

`last`

- List login information of a specific user:

`last {{username}}`

- Specify how many of the last logins to show:

`last {{[-n|--limit]}} {{login_count}}`

- Print the full date and time for entries and then display the hostname column last to prevent truncation:

`last {{[-F|--fulltimes]}} {{[-a|--hostlast]}}`

- View all logins by a specific user and show the IP address instead of the hostname:

`last {{username}} {{[-i|--ip]}}`

- List information since a specific time and date:

`last {{[-s|--since]}} {{-7days}}`

- View all recorded reboots (i.e., the last logins of the pseudo user "reboot"):

`last reboot`

- Display help:

`last {{[-h|--help]}}`
