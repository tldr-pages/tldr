# mocp

> Music on Console (MOC) 오디오 플레이어.
> 더 많은 정보: <https://manned.org/mocp>.

- MOC 터미널 UI 실행:

`mocp`

- 특정 디렉토리에서 MOC 터미널 UI 실행:

`mocp {{경로/대상/폴더}}`

- MOC 터미널 UI를 실행하지 않고 백그라운드에서 MOC 서버 시작:

`mocp --server`

- MOC가 백그라운드에서 실행 중일 때 특정 곡을 재생 목록에 추가:

`mocp --enqueue {{경로/대상/오디오_파일}}`

- MOC가 백그라운드에서 실행 중일 때 재귀적으로 곡을 재생 목록에 추가:

`mocp --append {{경로/대상/폴더}}`

- MOC가 백그라운드에서 실행 중일 때 재생 목록 지우기:

`mocp --clear`

- MOC가 백그라운드에서 실행 중일 때 현재 대기 중인 곡 재생 또는 정지:

`mocp --{{play|stop}}`

- MOC 서버를 백그라운드에서 중지:

`mocp --exit`
