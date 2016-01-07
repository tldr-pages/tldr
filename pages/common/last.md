# last

> View the last logged in users.

- View last logins, their duration  and other information as read from /var/log/wtmp:

`last`

- Specify how many of the last logins to show:

`last -n {{login_count}}`

- View full login times and dates:

`last -F`

- View the last login by a specific user:

`last {{user_name}}`

- View the last reboot (last login of the pseudo user reboot):

`last reboot`

- View the last shutdown (last login of the pseudo user shutdown):

`last shutdown`
