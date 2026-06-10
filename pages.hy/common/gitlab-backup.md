# gitlab-backup

> Կառավարեք պահուստները GitLab Omnibus-ի տեղադրման համար:.
> Տես նաև՝ `gitlab-ctl`, `gitlab-runner`:.
> Լրացուցիչ տեղեկություններ. <https://docs.gitlab.com/administration/backup_restore/backup_gitlab/>:.

- Ստեղծեք ամբողջական կրկնօրինակում (կանխադրված ռազմավարություն).:

`sudo gitlab-backup create`

- Ստեղծեք ամբողջական կրկնօրինակում, օգտագործելով պատճենման ռազմավարությունը.:

`sudo gitlab-backup create STRATEGY={{copy}}`

- Վերականգնել կրկնօրինակը` նշելով դրա ID-ն.:

`sudo gitlab-backup restore BACKUP={{backup_id}}`

- Վերականգնել կրկնօրինակը հատուկ բաղադրիչները բաց թողնելիս.:

`sudo gitlab-backup restore BACKUP={{backup_id}} SKIP={{db,uploads,...}}`
