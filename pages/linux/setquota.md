# setquota

> Set disk quotas for users, groups, or projects.
> Only the super-user may edit quotas.
> More information: <https://man7.org/linux/man-pages/man8/setquota.8.html>.

- Set a user's block quota, leaving inode limits disabled:

`sudo setquota {{username}} {{100G}} {{110G}} 0 0 {{filesystem}}`

- Set a group's block and inode quotas:

`sudo setquota {{[-g|--group]}} {{group}} {{100G}} {{110G}} {{50k}} {{60k}} {{filesystem}}`

- Set a project quota:

`sudo setquota {{[-P|--project]}} {{project}} {{100G}} {{110G}} 0 0 {{filesystem}}`

- Copy quota limits from one user to another:

`sudo setquota {{[-p|--prototype]}} {{reference_user}} {{username}} {{filesystem}}`

- Set the block and inode grace periods in seconds:

`sudo setquota {{[-t|--edit-period]}} {{604800}} {{604800}} {{filesystem}}`

- Disable all quota limits for a user:

`sudo setquota {{username}} 0 0 0 0 {{filesystem}}`
