# usermod

> 사용자 계정을 수정합니다.
> 같이 보기: `users`, `useradd`, `userdel`.
> 더 많은 정보: <https://manned.org/usermod>.

- 사용자명을 변경:

`sudo usermod {{[-l|--login]}} {{새로운_사용자명}} {{사용자명}}`

- 사용자 ID 변경:

`sudo usermod {{[-u|--uid]}} {{ID}} {{사용자명}}`

- 사용자 셸 변경:

`sudo usermod {{[-s|--shell]}} {{경로/대상/셸}} {{사용자명}}`

- 사용자를 보조 그룹에 추가 (공백 없음에 유의):

`sudo usermod {{[-a|--append]}} {{[-G|--groups]}} {{그룹1,그룹2,...}} {{사용자명}}`

- 사용자 홈 디렉터리 변경:

`sudo usermod {{[-m|--move-home]}} {{[-d|--home]}} {{경로/대상/새로운_홈}} {{사용자명}}`
