# vpnd

> 수신 VPN 연결을 대기합니다.
> 수동으로 실행하지 마십시오.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/vpnd.8.html>.

- 데몬 시작:

`vpnd`

- 포그라운드에서 데몬 실행:

`vpnd -x`

- 포그라운드에서 데몬을 실행하고 로그를 터미널에 출력:

`vpnd -d`

- 포그라운드에서 데몬을 실행하고 로그를 터미널에 출력하며 인수를 검증한 후 종료:

`vpnd -n`

- 특정 서버 설정으로 데몬 실행:

`vpnd -i {{서버_ID}}`

- 도움말 표시:

`vpnd -h`
