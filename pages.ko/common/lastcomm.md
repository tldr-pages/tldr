# lastcomm

> 마지막으로 실행된 명령어를 표시.
> 더 많은 정보: <https://manpages.debian.org/latest/acct/lastcomm.1.en.html>.

- acct (기록 파일)에 있는 모든 명령어 정보 출력:

`lastcomm`

- 특정 사용자가 실행한 명령어 표시:

`lastcomm --user {{사용자}}`

- 시스템에서 실행된 특정 명령어 정보 표시:

`lastcomm --command {{명령어}}`

- 특정 터미널에서 실행된 명령어 정보 표시:

`lastcomm --tty {{터미널_이름}}`
