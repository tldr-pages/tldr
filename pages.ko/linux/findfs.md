# findfs

> 파일시스템을 레이블 또는 UUID로 찾습니다.
> 더 많은 정보: <https://manned.org/findfs>.

- 파일시스템 레이블로 블록 장치 검색:

`findfs LABEL={{레이블}}`

- 파일시스템 UUID로 검색:

`findfs UUID={{uuid}}`

- 파티션 레이블로 검색 (GPT 또는 MAC 파티션 테이블):

`findfs PARTLABEL={{파티션_레이블}}`

- 파티션 UUID로 검색 (GPT 파티션 테이블 전용):

`findfs PARTUUID={{파티션_uuid}}`
