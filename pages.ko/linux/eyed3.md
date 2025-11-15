# eyeD3

> MP3 파일의 메타데이터를 읽고 조작합니다.
> 더 많은 정보: <https://manned.org/eyeD3>.

- MP3 파일의 정보 보기:

`eyeD3 {{파일명.mp3}}`

- MP3 파일의 제목 설정:

`eyeD3 {{[-t|--title]}} "{{제목}}" {{파일명.mp3}}`

- 폴더 내 모든 MP3 파일의 앨범 설정:

`eyeD3 {{[-A|--album]}} "{{앨범_이름}}" {{*.mp3}}`

- MP3 파일의 앞면 커버 이미지 설정:

`eyeD3 --add-image {{앞면_커버.jpeg}}:FRONT_COVER: {{파일명.mp3}}`
