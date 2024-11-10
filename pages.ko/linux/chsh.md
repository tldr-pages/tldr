# chsh

> 사용자의 로그인 셸 변경.
> `util-linux`의 일부.
> 더 많은 정보: <https://manned.org/chsh>.

- 현재 사용자에 대해 특정 로그인 셸을 대화식으로 설정:

`chsh`

- 현재 사용자에 대해 특정 로그인 [s]셸 설정:

`chsh --shell {{경로/대상/셸}}`

- 특정 사용자에 대해 로그인 [s]셸 설정:

`sudo chsh --shell {{경로/대상/셸}} {{사용자명}}`

- 사용 가능한 셸 [l]나열:

`chsh --list-shells`
