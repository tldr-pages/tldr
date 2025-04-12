# chage

> Change user account and password expiry information.
> More information: <https://manned.org/chage>.

- List password information for the user:

`chage {{[-l|--list]}} {{username}}`

- Enable password expiration in 10 days:

`sudo chage {{[-M|--maxdays]}} {{10}} {{username}}`

- Disable password expiration:

`sudo chage {{[-M|--maxdays]}} {{-1}} {{username}}`

- Set account expiration date:

`sudo chage {{[-E|--expiredate]}} {{YYYY-MM-DD}} {{username}}`

- Force user to change password on next log in:

`sudo chage {{[-d|--lastday]}} {{0}} {{username}}`

- Re-enable an account:

`sudo chage {{[-E|--expiredate]}} -1 {{username}}`
