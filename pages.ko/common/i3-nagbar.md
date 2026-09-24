# i3-nagbar

> 화면 상단에 오류/경고 메시지를 바 형태로 표시.
> 더 많은 정보: <https://manned.org/i3-nagbar>.

- 오류 메시지 표시:

`i3-nagbar {{[-m|--message]}} "{{에러 메시지}}"`

- 경고 메시지 표시:

`i3-nagbar {{[-t|--type]}} warning {{[-m|--message]}} "{{경고 메시지}}"`

- 지정한 폰트 사용:

`i3-nagbar {{[-f|--font]}} "{{pango:monospace bold 9}}" {{[-m|--message]}} "{{에러 메시지}}"`

- 버튼 생성 후 클릭 시, 터미널에서 명령 실행:

`i3-nagbar {{[-b|--button]}} "{{버튼 텍스트}}" {{명령어}} {{[-m|--message]}} "{{에러 메시지}}"`

- 버튼 생성 후 클릭 시 터미널 없이 명령 실행:

`i3-nagbar {{[-B|--button-no-terminal]}} "{{버튼 텍스트}}" {{명령어}} {{[-m|--message]}} "{{에러 메시지}}"`

- 항상 기본 모니터에서 `i3-nagbar` 실행 (기본값: 현재 포커스가 된 모니터):

`i3-nagbar {{[-pm|--primary --message]}} "{{에러 메시지}}"`
