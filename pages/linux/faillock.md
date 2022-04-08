# faillock

> Display and modify authentication failure record files.
> More information: <https://github.com/linux-pam/linux-pam>.

- List login failures of all users:

`sudo faillock`

- List login failures of the specified user:

`sudo faillock --user {{user}}`

- Reset specified user's failure records:

`sudo faillock --user {{user}} --reset`
