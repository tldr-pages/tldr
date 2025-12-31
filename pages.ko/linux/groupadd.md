# groupadd

> 시스템에 사용자 그룹 추가.
> 같이 보기: `groups`, `groupdel`, `groupmod`.
> 더 많은 정보: <https://manned.org/groupadd>.

- 새 그룹 생성:

`sudo groupadd {{그룹_이름}}`

- 새 시스템 그룹 생성:

`sudo groupadd {{[-r|--system]}} {{그룹_이름}}`

- 특정 그룹 ID로 새 그룹 생성:

`sudo groupadd {{[-g|--gid]}} {{ID}} {{그룹_이름}}`
