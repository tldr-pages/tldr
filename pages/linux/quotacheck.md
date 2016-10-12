# quotacheck

> Scan a filesystem for disk usage; create, check and repair quota files.
> It is best to run quota check with quotas turned off to prevent damage or loss to quota files.

- Check all mounted non-NFS filesystems:

`sudo quotacheck --all`

- Force check even if quotas are enabled:

`sudo quotacheck --force {{filesystem}}`

- Check quotas on a given filesystem in debug mode:

`sudo quotacheck --debug {{filesystem}}`

- Report progress as quotacheck progresses:

`sudo quotacheck --verbose {{filesystem}}`

- Check user quotas:

`sudo quotacheck --user {{user}} {{filesystem}}`

- Check group quotas:

`sudo quotacheck --group {{group}} {{filesystem}}`
