# ghostty

> 플랫폼 네이티브 UI와 GPU 가속을 사용하는 빠르고 기능이 풍부한, 크로스 플랫폼 터미널 에뮬레이터.
> 참고: 설정 파일의 모든 옵션은 명령줄에서도 `--option=argument` 형식으로 사용 가능.
> 더 많은 정보: <https://ghostty.org/docs/config/reference>.

- 새로운 Ghostty 창 열기 (macOS에서는 지원되지 않음):

`ghostty`

- 새로운 Ghostty 창에서 특정 명령 실행 (macOS에서는 지원되지 않음):

`ghostty -e {{명령어}}`

- 기본 및 사용자 설정 키바인딩 목록 표시:

`ghostty +list-keybinds`

- 모든 액션(키바인딩으로 실행 가능한 기능) 목록 표시:

`ghostty +list-actions`

- 대화형 테마 목록 탐색:

`ghostty +list-themes`

- 기본 설정 전체 출력 (주석 포함):

`ghostty +show-config --default --docs`
