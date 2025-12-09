# blockdev

> 블록 장치를 관리, 조회 및 조작.
> 더 많은 정보: <https://manned.org/blockdev>.

- 모든 장치에 대한 보고서 출력:

`sudo blockdev --report`

- 특정 장치에 대한 보고서 출력:

`sudo blockdev --report {{/dev/sdXY}}`

- 장치의 크기를 512바이트 섹터 단위로 확인:

`sudo blockdev --getsz {{/dev/sdXY}}`

- 읽기 전용으로 설정:

`sudo blockdev --setro {{/dev/sdXY}}`

- 읽기-쓰기 가능으로 설정:

`sudo blockdev --setrw {{/dev/sdXY}}`

- 버퍼 플러시:

`sudo blockdev --flushbufs {{/dev/sdXY}}`

- 물리적 블록 크기 확인:

`sudo blockdev --getpbsz {{/dev/sdXY}}`

- 선행 읽기 값을 128 섹터로 설정:

`sudo blockdev --setra 128 {{/dev/sdXY}}`
