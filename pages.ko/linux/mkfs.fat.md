# mkfs.fat

> 파티션 내에 MS-DOS 파일 시스템 생성.
> 더 많은 정보: <https://manned.org/mkfs.fat>.

- 장치 b의 파티션 1 (`sdb1`) 에 fat 파일 시스템 생성:

`mkfs.fat {{/dev/sdb1}}`

- 볼륨 이름을 지정하여 파일 시스템 생성:

`mkfs.fat -n {{볼륨_이름}} {{/dev/sdb1}}`

- 볼륨 ID를 지정하여 파일 시스템 생성:

`mkfs.fat -i {{볼륨_ID}} {{/dev/sdb1}}`

- 파일 할당 테이블을 2개 대신 5개 사용:

`mkfs.fat -f 5 {{/dev/sdb1}}`
