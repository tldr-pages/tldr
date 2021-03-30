# atq

> Show jobs scheduled by `at` or `batch` commands.
> More information: <https://man.archlinux.org/man/at.1>.

- Show the current user's scheduled jobs:

`atq`

- Show jobs from queue named 'a' (queues have single-character names):

`atq -q {{a}}`

- Show jobs of all users (run as super user):

`sudo atq`
