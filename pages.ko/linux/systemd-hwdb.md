# systemd-hwdb

> 하드웨어 데이터베이스 관리 도구.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-hwdb.html>.

- `/etc/udev`의 바이너리 하드웨어 데이터베이스 업데이트:

`systemd-hwdb update`

- 하드웨어 데이터베이스를 조회하고 특정 모달리아스에 대한 결과 출력:

`systemd-hwdb query {{모달리아스}}`

- 구문 오류 발생 시 0이 아닌 종료 값을 반환하며 바이너리 하드웨어 데이터베이스 업데이트:

`systemd-hwdb --strict update`

- `/usr/lib/udev`의 바이너리 하드웨어 데이터베이스 업데이트:

`systemd-hwdb --usr update`

- 지정된 루트 경로의 바이너리 하드웨어 데이터베이스 업데이트:

`systemd-hwdb --root={{경로/대상/루트}} update`
