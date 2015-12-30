# last 

> View the last logged in users

- view last logins, their duration  and other information as read from /var/log/wtmp

`last`

- specify how many of the last logins to show

`last -n {{login_count}}`

- view full login times and dates 

`last -F`

- view the last login by a specific user

`last {{user_name}}`

- view the last reboot (last login of the pseudo user reboot)

`last reboot`

- view the last shutdown (last login of the pseudo user shutdown)

`last shutdown`
