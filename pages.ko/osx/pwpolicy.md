# pwpolicy

> 비밀번호 정책을 조회하고 설정.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/pwpolicy.8.html>.

- 지정한 사용자의 비밀번호 변경:

`sudo pwpolicy -a {{authenticator}} -u {{사용자명}} -setpassword "{{새로운_비밀번호}}"`

- 사용자 계정 비활성화:

`sudo pwpolicy -u {{사용자명}} -disableuser`

- 사용자 계정 활성화:

`sudo pwpolicy -u {{사용자명}} -enableuser`

- 사용자 계정에 대해 디스크에 저장된 비밀번호 해시 유형 목록 조회:

`sudo pwpolicy -u {{사용자명}} -gethashtypes`
