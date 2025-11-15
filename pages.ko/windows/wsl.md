# wsl

> Windows Subsystem for Linux를 관리합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows/wsl/reference>.

- Linux 쉘 시작 (기본 배포판):

`wsl {{쉘_명령어}}`

- 쉘을 사용하지 않고 Linux 명령 실행:

`wsl --exec {{명령어}} {{명령어_인수}}`

- 특정 배포판 지정:

`wsl --distribution {{배포판}} {{쉘_명령어}}`

- 사용 가능한 배포판 나열:

`wsl --list`

- 배포판을 `.tar` 파일로 내보내기:

`wsl --export {{배포판}} {{경로\배포판_파일이름.tar}}`

- `.tar` 파일에서 배포판 가져오기:

`wsl --import {{배포판}} {{경로\설치_위치}} {{경로\배포판_파일이름.tar}}`

- 특정 배포판에 대해 사용되는 wsl 버전 변경:

`wsl --set-version {{배포판}} {{버전}}`

- Windows Subsystem for Linux 종료:

`wsl --shutdown`
