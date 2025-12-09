# duplicacy

> 잠금 없는 중복 제거 클라우드 백업 도구.
> 더 많은 정보: <https://github.com/gilbertchen/duplicacy/wiki>.

- 현재 디레터리를 저장소로 사용하고, SFTP 저장소를 초기화하고, 저장소를 비밀번호로 암호화:

`duplicacy init -e {{snapshot_id}} {{sftp://user@192.168.2.100/path/to/storage/}}`

- 저장소의 스냅샷을 기본 저장소에 저장:

`duplicacy backup`

- 현재 저장소의 스냅샷 목록:

`duplicacy list`

- 이전에 저장된 스냅샷으로 저장소를 복원:

`duplicacy restore -r {{revision}}`

- 스냅샷의 무결성을 확인:

`duplicacy check`

- 기존 저장소에 사용할 다른 저장소를 추가:

`duplicacy add {{스토리지_이름}} {{스냅샷_아이디}} {{스토리지_주소}}`

- 스냅샷의 특정 버전을 정리:

`duplicacy prune -r {{버전}}`

- `m`일보다 오래된 버전에 대해 `n`일마다 하나의 업데이트된 버전을 유지하여 버전을 정리:

`duplicacy prune -keep {{n:m}}`
