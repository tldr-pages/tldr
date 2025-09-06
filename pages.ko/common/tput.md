# tput

> 터미널 설정 및 기능을 조회하고 수정.
> 더 많은 정보: <https://manned.org/tput>.

- 커서를 특정 화면 위치로 이동:

`tput cup {{행}} {{열}}`

- 전경색(af) 또는 배경색(ab) 설정:

`tput {{setaf|setab}} {{ANSI_색상_코드}}`

- 컬럼 수, 라인 수, 또는 색상 수 표시:

`tput {{cols|lines|colors}}`

- 터미널 벨 울리기:

`tput bel`

- 모든 터미널 속성 초기화:

`tput sgr0`

- 자동 줄바꿈 활성화 또는 비활성화:

`tput {{smam|rmam}}`
