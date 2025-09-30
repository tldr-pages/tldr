# cfdisk

> curses UI를 사용하여 하드 디스크의 파티션 테이블 및 파티션을 관리.
> 더 많은 정보: <https://manned.org/cfdisk>.

- 특정 장치로 파티션 조작기 시작:

`cfdisk {{/dev/sdX}}`

- 특정 장치에 대한 새 파티션 테이블 생성 및 관리:

`cfdisk {{[-z|--zero]}} {{/dev/sdX}}`
