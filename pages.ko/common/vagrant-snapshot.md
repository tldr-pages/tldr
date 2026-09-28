# vagrant snapshot

> Vagrant machine의 snapshot을 관리.
> 관련 항목: `vagrant`.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/snapshot>.

- machine의 현재 상태를 snapshot으로 저장 (실행 또는 중지 상태 모두 가능):

`vagrant snapshot save {{snapshot_이름}}`

- snapshot을 복원하고 machine 시작:

`vagrant snapshot restore {{snapshot_이름}}`

- machine을 시작하지 않고 snapshot 복원:

`vagrant snapshot restore --no-start {{snapshot_이름}}`

- snapshot 삭제:

`vagrant snapshot delete {{snapshot_이름}}`

- machine에서 사용 가능한 snapshot 목록 표시:

`vagrant snapshot list`
