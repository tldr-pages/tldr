# sa

> Summarizes accounting information. Part of the acct package.
> Shows commands called by users, including basic info on CPU time spent processing and I/O rates.
> More information: <https://manned.org/man/sa.8>.

- Display executable invocations per user (username not displayed):

`sudo sa`

- Display executable invocations per user, showing responsible usernames:

`sudo sa --print-users`

- List resources used recently per user:

`sudo sa --user-summary`
