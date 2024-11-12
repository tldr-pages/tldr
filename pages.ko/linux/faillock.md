# faillock

> 인증 실패 기록 파일을 표시하고 수정합니다.
> 더 많은 정보: <https://manned.org/faillock>.

- 현재 사용자의 로그인 실패 목록 표시:

`faillock`

- 현재 사용자의 실패 기록 초기화:

`faillock --reset`

- 모든 사용자의 로그인 실패 목록 표시:

`sudo faillock`

- 특정 사용자의 로그인 실패 목록 표시:

`sudo faillock --user {{사용자}}`

- 특정 사용자의 실패 기록 초기화:

`sudo faillock --user {{사용자}} --reset`
