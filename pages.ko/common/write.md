# write

> 지정된 로그인 사용자에게 터미널에 메시지를 작성합니다 (`<Ctrl c>`로 메시지 작성을 중단할 수 있음).
> 시스템에서 활성 사용자들의 모든 터미널 ID를 확인하려면 `who` 명령을 사용하세요. 같이 보기: `mesg`.
> 더 많은 정보: <https://manned.org/write.1p>.

- 지정된 사용자에게 주어진 터미널 ID로 메시지 전송:

`write {{사용자_명}} {{터미널_ID}}`

- 터미널 `/dev/tty/5`에서 "testuser"에게 메시지 전송:

`write {{testuser}} {{tty/5}}`

- 의사 터미널 `/dev/pts/5`에서 "johndoe"에게 메시지 전송:

`write {{johndoe}} {{pts/5}}`
