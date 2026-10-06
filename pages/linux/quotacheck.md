# quotacheck

> Scan a filesystem for disk usage; create, check, and repair quota files.
> It is best to run quota check with quotas turned off to prevent damage or loss to quota files.
> More information: <https://manned.org/quotacheck>.

- Check quotas on all mounted non-NFS filesystems:

`sudo quotacheck --all`

- Force check even if quotas are enabled (this can cause damage or loss to quota files):

`sudo quotacheck --force {{path/to/mount_point}}`

- Check quotas on a given filesystem in debug mode:

`sudo quotacheck --debug {{path/to/mount_point}}`

- Check quotas on a given filesystem, displaying the progress:

`sudo quotacheck --verbose {{path/to/mount_point}}`

- Check user quotas:

`sudo quotacheck --user {{user}} {{path/to/mount_point}}`

- Check group quotas:

`sudo quotacheck --group {{group}} {{path/to/mount_point}}`
