# tlmgr

> 기존 TeX Live 설치의 패키지 및 구성 옵션 관리.
> `paper`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#ACTIONS>.

- 패키지 및 그 의존성 설치:

`tlmgr install {{패키지}}`

- 패키지 및 그 의존성 제거:

`tlmgr remove {{패키지}}`

- 패키지에 대한 정보 표시:

`tlmgr info {{패키지}}`

- 모든 패키지 업데이트:

`tlmgr update --all`

- 업데이트 가능한 항목을 표시하지만 실제로 업데이트하지 않음:

`tlmgr update --list`

- tlmgr의 GUI 버전 시작:

`tlmgr gui`

- 모든 TeX Live 구성 나열:

`tlmgr conf`
