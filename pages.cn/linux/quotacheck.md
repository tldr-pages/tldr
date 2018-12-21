# quotacheck

> Scan a filesystem for disk usage; create, check and repair quota files.
> It is best to run quota check with quotas turned off to prevent damage or loss to quota files.

- Check quotas on all mounted non-NFS filesystems:

`sudo quotacheck --all`

- Force check even if quotas are enabled (this can cause damage or loss to quota files):

`sudo quotacheck --force {{mountpoint}}`

- Check quotas on a given filesystem in debug mode:

`sudo quotacheck --debug {{mountpoint}}`

- Check quotas on a given filesystem, displaying the progress:

`sudo quotacheck --verbose {{mountpoint}}`

- Check user quotas:

`sudo quotacheck --user {{user}} {{mountpoint}}`

- Check group quotas:

`sudo quotacheck --group {{group}} {{mountpoint}}`
