# gitlab-backup

> Управлять резервными копиями установки GitLab Omnibus.
> Смотрите также: `gitlab-ctl`, `gitlab-runner`.
> Больше информации: <https://docs.gitlab.com/administration/backup_restore/backup_gitlab/>.

- Создать полную резервную копию (стратегия по умолчанию):

`sudo gitlab-backup create`

- Создать полную резервную копию, используя стратегию копирования:

`sudo gitlab-backup create STRATEGY={{copy}}`

- Восстановить резервную копию, указав её идентификатор:

`sudo gitlab-backup restore BACKUP={{идентификатор_копии}}`

- Восстановить резервную копию, пропустив конкретные компоненты:

`sudo gitlab-backup restore BACKUP={{идентификатор_копии}} SKIP={{db,uploads,...}}`
