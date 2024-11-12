# opensnoop

> 시스템에서 파일 열림을 추적합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/opensnoop.1m.html>.

- 파일이 열릴 때마다 모두 출력:

`sudo opensnoop`

- 프로세스 이름으로 파일 열림 추적:

`sudo opensnoop -n "{{프로세스_이름}}"`

- PID로 파일 열림 추적:

`sudo opensnoop -p {{PID}}`

- 특정 파일을 여는 프로세스 추적:

`sudo opensnoop -f {{경로/대상/파일}}`
