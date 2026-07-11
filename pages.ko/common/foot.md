# foot

> 빠르고, 가벼우며, 최소한의 기능을 제공하는 Wayland 터미널 에뮬레이터.
> 더 많은 정보: <https://manned.org/foot>.

- 터미널 실행:

`foot`

- 서버 시작 (`footclient`를 사용하여 서버에 연결되는 터미널 창 실행):

`foot {{[-s|--server]}}`

- 새로운 터미널 창에서 명령 실행:

`foot {{명령어}}`

- 전체 화면 모드로 터미널 실행:

`foot {{[-F|--fullscreen]}}`

- 지정한 창 크기(픽셀)로 터미널 실행:

`foot {{[-w|--window-size-pixels]}} {{너비}}x{{높이}}`

- 지정한 Wayland 애플리케이션 ID로 터미널 실행 (기본값: `foot`):

`foot {{[-a|--app-id]}} {{아이디}}`

- 설정 파일 오류 검사:

`foot {{[-C|--check-config]}}`

- 설정 옵션 재정의:

`foot {{[-o|--override]}} {{섹션}}.{{키}}={{값}}`
