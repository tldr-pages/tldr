# lchage

> Display or change user password policy.
> More information: <https://manned.org/lchage>.

- Disable password expiration for the user:

`sudo lchage --date -1 {{username}}`

- Display the password policy for the user:

`sudo lchage --list {{username}}`

- Require password change for the user a certain number of days after the last password change:

`sudo lchage --maxdays {{number_of_days}} {{username}}`

- Start warning the user a certain number of days before the password expires:

`sudo lchage --warndays {{number_of_days}} {{username}}`
