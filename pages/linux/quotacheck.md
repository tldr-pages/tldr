# quotacheck

> Scan a filesystem for disk usage; create, check and repair quota files.
> Should only be run by the super-user.

- Check all mounted non-NFS filesystems:

`quotacheck --all`

- Force check even if quotas are enabled:

`quotacheck --force {{filesystem}}`

- Enable debugging mode:

`quotacheck --debug {{filesystem}}`

- Report progress as quotacheck progresses:

`quotacheck --verbose {{filesystem}}`

- Check user quotas (default):

`quotacheck --user {{user}} {{filesystem}}`

- Check group quotas:

`quotacheck --group {{group}} {{filesystem}}`
