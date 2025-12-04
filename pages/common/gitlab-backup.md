# gitlab-backup

> Manage backups for a GitLab Omnibus installation.
> See also: `gitlab-ctl`, `gitlab-rake`, `gitlab-runner`.
> More information: <https://docs.gitlab.com/administration/backup_restore/backup_gitlab/>.

- Create a full backup (default strategy):

`sudo gitlab-backup create`

- Create a full backup using the copy strategy:

`sudo gitlab-backup create STRATEGY={{copy}}`

- Restore a backup by specifying its ID:

`sudo gitlab-backup restore BACKUP={{backup_id}}`

- Restore a backup while skipping specific components:

`sudo gitlab-backup restore BACKUP={{backup_id}} SKIP={{db,uploads,...}}`

- Trigger a backup from within a running GitLab Docker container:

`docker exec -t {{gitlab_container}} gitlab-backup create`
