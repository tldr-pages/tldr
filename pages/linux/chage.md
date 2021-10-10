# chage

> Change user account and password expiry information.
> More information: <https://manned.org/chage>.

- List password information for the user:

`chage --list {{username}}`

- Enable password expiration in 10 days:

`sudo chage --maxdays {{10}} {{username}}`

- Disable password expiration:

`sudo chage --maxdays {{-1}} {{username}}`

- Set account expiration date:

`sudo chage --expiredate {{YYYY-MM-DD}} {{username}}`

- Force user to change password on next log in:

`sudo chage --lastday {{0}} {{username}}`
