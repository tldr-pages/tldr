# xxh

> SSH 세션을 통해 모든 사용자 정의 설정과 함께 셸을 사용하세요.
> 참고: xxh는 대상 머신의 시스템 디렉토리에 아무것도 설치하지 않습니다; `~/.xxh`를 제거하면 대상 머신에서 xxh의 모든 흔적이 제거됩니다.
> 더 많은 정보: <https://github.com/xxh/xxh#usage>.

- 호스트에 연결하고 현재 셸 실행:

`xxh "{{호스트}}"`

- 대화 상자 없이 현재 셸을 대상 머신에 설치:

`xxh "{{호스트}}" ++install`

- 대상 머신에서 지정된 셸 실행:

`xxh "{{호스트}}" ++shell {{xonsh|zsh|fish|bash|osquery}}`

- 대상 머신에서 특정 xxh 구성 디렉토리 사용:

`xxh "{{호스트}}" ++host-xxh-home {{~/.xxh}}`

- 호스트 머신에서 지정된 구성 파일 사용:

`xxh "{{호스트}}" ++xxh-config {{~/.config/xxh/config.xxhc}}`

- SSH 연결에 사용할 비밀번호 지정:

`xxh "{{호스트}}" ++password "{{비밀번호}}"`

- 대상 머신에 xxh 패키지 설치:

`xxh "{{호스트}}" ++install-xxh-packages {{패키지}}`

- 대상 머신의 셸 프로세스에 대한 환경 변수 설정:

`xxh "{{호스트}}" ++env {{이름}}={{값}}`
