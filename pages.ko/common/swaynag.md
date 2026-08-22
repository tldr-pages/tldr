# swaynag

> 화면 상단 바에 메시지 표시.
> 더 많은 정보: <https://github.com/swaywm/sway/blob/master/swaynag/swaynag.1.scd>.

- 오류 메시지 표시:

`swaynag {{[-m|--message]}} "{{error message}}"`

- 경고 메시지 표시:

`swaynag {{[-t|--type]}} warning {{[-m|--message]}} "{{warning message}}"`

- 설정 파일에 정의된 사용자 지정 타입으로 메시지 표시:

`swaynag {{[-t|--type]}} {{custom_type}} {{[-m|--message]}} "{{message}}"`

- 지정한 글꼴을 사용하여 메시지 표시:

`swaynag {{[-f|--font]}} "{{monospace bold 9}}" {{[-m|--message]}} "{{에러 메시지}}"`

- 버튼을 생성하고 클릭 시 지정한 터미널에서 명령 실행:

`TERMINAL={{terminal_executable}} swaynag {{[-b|--button]}} "{{버튼 텍스트}}" {{명령어}} {{[-m|--message]}} "{{에러 메시지}}"`

- 버튼을 생성하고 클릭 시 터미널 없이 명령 실행:

`swaynag {{[-B|--button-no-terminal]}} "{{버튼 텍스트}}" {{명령어}} {{[-m|--message]}} "{{에러 메시지}}"`

- 화면 하단에 바 표시:

`swaynag {{[-e|--edge]}} bottom {{[-m|--message]}} "{{에러 메시지}}"`

- 지정한 모니터에서 `swaynag` 열기:

`swaynag {{[-o|--output]}} {{DP-1}} {{[-m|--message]}} "{{에러 메시지}}"`
