# clinfo

> OpenCL 플랫폼 및 장치 정보 표시.
> 더 많은 정보: <https://manned.org/clinfo>.

- 모든 OpenCL 플랫폼과 장치 정보 표시:

`clinfo`

- 플랫폼과 장치를 이름별로 목록 표시:

`clinfo {{[-l|--list]}}`

- 지정한 장치의 정보 표시:

`clinfo {{[-d|--device]}} {{플랫폼_인덱스}}:{{장치_인덱스}}`

- 머신이 처리하기 쉬운 형식으로 출력:

`clinfo --raw`

- 오프라인 장치 포함:

`clinfo --offline`

- 비공식 속성을 포함한 모든 속성 조회 시도:

`clinfo {{[-a|--all-props]}}`

- 지정한 속성 이름과 일치하는 속성만 표시:

`clinfo --prop {{속성_이름}}`
