# setquota

> Set disk quotas for a user or group.
> More information: <https://manned.org/setquota>.

- Edit remote quota over RPC, uses rpc.quotad on the remote host to set quota:

`setquota -r, --remote`

- Set user quotas for named user:

`setquota --user {{username}} {{block_soft_limit}} {{block_hard_limit}} {{inode_soft_limit}} {{inode_hard_limit}} {{path/to/directory}}`

- Set group quotas for named group:

`setquota -g, --group`

- Use quota settings of user, group or project to set the quota for the named user, group or project:

`setquota -p, --prototype={{protoname}}`

- Go through all filesystems with quotas in `/etc/mtab` and perform the setting:

`setquota -a, --all`
