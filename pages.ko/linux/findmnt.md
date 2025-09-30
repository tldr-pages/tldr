# findmnt

> 파일 시스템을 찾습니다.
> 더 많은 정보: <https://manned.org/findmnt>.

- 모든 마운트된 파일 시스템 나열:

`findmnt`

- 디바이스 검색:

`findmnt {{/dev/sdb1}}`

- 마운트 지점 검색:

`findmnt {{/}}`

- 특정 유형의 파일 시스템 찾기:

`findmnt -t {{ext4}}`

- 특정 레이블이 있는 파일 시스템 찾기:

`findmnt LABEL={{BigStorage}}`

- 마운트 테이블 내용을 자세히 확인하고 `/etc/fstab` 검증:

`findmnt --verify --verbose`
