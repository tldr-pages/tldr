# lchage

> Display or change user password policy.
> More information: <https://manned.org/lchage>.

- Disable password expiration for the user:

`sudo lchage --date -1 {{username}}`

- List password policy for the user:

`sudo lchage --list {{username}}`

- Require password change for a user, certain days after the last password change:

`sudo lchage --maxdays={{number_of_days}} {{username}}`

- Start warning the user certain days before the password expires:

`sudo lchage --warndays={{number_of_days}} {{username}}`
