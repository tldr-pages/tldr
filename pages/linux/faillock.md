# faillock

> Display and modify authentication failure record files.
> More information: <https://manned.org/faillock>.

- List login failures of the current user:

`faillock`

- Reset the failure records of the current user:

`faillock --reset`

- List login failures of all users:

`sudo faillock`

- List login failures of the specified user:

`sudo faillock --user {{user}}`

- Reset the failure records of the specified user:

`sudo faillock --user {{user}} --reset`
