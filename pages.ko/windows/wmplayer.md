# wmplayer

> Windows Media Player를 사용하여 미디어 파일을 재생하고 관리.
> 참고: 이 명령은 Windows 10 이전 버전의 Windows Media Player에서만 사용 가능.
> 더 많은 정보: <https://learn.microsoft.com/previous-versions/windows/desktop/wmp/command-line-parameters>.

- Windows Media Player 실행:

`wmplayer`

- 오디오, 비디오 또는 재생 목록 파일 재생:

`wmplayer {{경로\대상\파일}}`

- DVD 또는 오디오 CD 재생:

`wmplayer /device:{{dvd|audiocd}}`

- 전체 화면 모드로 파일 재생:

`wmplayer {{경로\대상\파일}} /fullscreen`

- 지정한 사용자 인터페이스 스킨을 적용하여 파일 재생:

`wmplayer "{{경로\대상\파일}}?wmpskin={{스킨_이름}}"`

- 미디어 라이브러리 페이지 표시:

`wmplayer /Task MediaLibrary`

- 현재 재생 페이지 표시:

`wmplayer /Task NowPlaying`
