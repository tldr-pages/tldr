# tput

> 터미널 설정 및 기능을 조회하고 수정.
> 관련 항목: `stty`.
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

- 터미널 커서를 숨기거나 표시:

`tput {{civis|cnorm}}`

- 터미널 텍스트 상태를 저장하거나 복원 (smcup은 스크롤 휠 이벤트도 캡처):

`tput {{smcup|rmcup}}`
