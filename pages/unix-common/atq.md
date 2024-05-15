# atq

> Show jobs scheduled by `at` or `batch` commands.
> More information: <https://manned.org/atq>.

- Show the current user's scheduled jobs:

`atq`

- Show jobs from the 'a' [q]ueue (queues have single-character names):

`atq -q {{a}}`

- Show jobs of all users (run as superuser):

`sudo atq`
