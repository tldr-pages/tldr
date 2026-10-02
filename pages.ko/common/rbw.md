# rbw

> Bitwarden와 호환되는 비공식 비밀번호 관리자.
> 더 많은 정보: <https://github.com/doy/rbw#configuration>.

- 볼트에 로그인:

`rbw login`

- 볼트 잠금 해제:

`rbw unlock`

- 볼트의 모든 항목 목록 표시:

`rbw list`

- 항목의 비밀번호 가져오기:

`rbw get "{{항목_이름}}"`

- 항목의 사용자 이름 가져오기:

`rbw get {{[-f|--field]}} username "{{항목_이름}}"`

- 항목의 비밀번호를 클립보드에 복사:

`rbw get {{[-c|--clipboard]}} "{{항목_이름}}"`

- 지정한 길이의 새로운 비밀번호 생성:

`rbw generate {{비밀번호_길이}}`

- 볼트 잠금:

`rbw lock`
