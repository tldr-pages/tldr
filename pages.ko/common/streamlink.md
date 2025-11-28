# streamlink

> 다양한 서비스에서 스트림을 추출하여 원하는 비디오 플레이어로 전달.
> 더 많은 정보: <https://streamlink.github.io/cli.html#command-line-usage>.

- 지정된 URL에서 스트림을 추출하고 성공하면 선택 가능한 스트림 목록 출력:

`streamlink {{example.com/stream}}`

- 지정된 품질로 스트림 열기:

`streamlink {{example.com/stream}} {{720p60}}`

- 사용할 수 있는 가장 높은 또는 낮은 품질 선택:

`streamlink {{example.com/stream}} {{best|worst}}`

- 특정 플레이어를 사용하여 스트림 데이터를 전달 (기본적으로 VLC가 발견되면 사용됨):

`streamlink --player={{mpv}} {{example.com/stream}} {{best}}`

- 스트림 시작 부분에서 특정 시간을 건너뜀. 라이브 스트림의 경우 스트림 끝에서부터 음수 오프셋(되감기):

`streamlink --hls-start-offset {{[HH:]MM:SS}} {{example.com/stream}} {{best}}`

- 라이브 스트림의 시작 부분으로 건너뛰거나 가능한 한 뒤로 이동:

`streamlink --hls-live-restart {{example.com/stream}} {{best}}`

- 스트림 데이터를 재생 대신 파일에 기록:

`streamlink --output {{경로/대상/파일.ts}} {{example.com/stream}} {{best}}`

- 스트림을 플레이어에서 열고 동시에 파일에 기록:

`streamlink --record {{경로/대상/파일.ts}} {{example.com/stream}} {{best}}`
