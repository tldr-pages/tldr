# gitlab-backup

> GitLab Omnibus 설치의 백업 관리.
> 관련 항목: `gitlab-ctl`, `gitlab-runner`.
> 더 많은 정보: <https://docs.gitlab.com/administration/backup_restore/backup_gitlab/>.

- 전체 백업 생성 (기본 전략을 사용):

`sudo gitlab-backup create`

- copy 전략을 사용하여 전체 백업 생성:

`sudo gitlab-backup create STRATEGY={{copy}}`

- 백업 ID를 지정하여 백업 복원:

`sudo gitlab-backup restore BACKUP={{백업_아이디}}`

- 특정 구성 요소를 제외하고 백업 복원:

`sudo gitlab-backup restore BACKUP={{백업_아이디}} SKIP={{db,uploads,...}}`
