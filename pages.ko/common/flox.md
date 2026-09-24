# flox

> 사용하기 쉬운 Nix 패키지 및 환경 관리자.
> 더 많은 정보: <https://flox.dev/docs/reference/command-reference/flox/>.

- 현재 디렉터리에 새로운 환경 생성:

`flox init`

- 환경에 진입하거나 환경이 존재하지 않으면, 새롭게 생성:

`flox activate`

- FloxHub 카탈로그에서 패키지 검색:

`flox search {{패키지}}`

- 현재 환경에 패키지 설치:

`flox {{[i|install]}} {{패키지}}`

- 현재 환경에서 패키지 제거:

`flox uninstall {{패키지}}`

- 현재 환경에 설치된 모든 패키지 목록 표시:

`flox {{[l|list]}}`

- FloxHub에 업로드하여 다른 사용자와 공유:

`flox push`

- FloxHub에서 공유된 환경 가져오기:

`flox pull {{환경_이름}}`
