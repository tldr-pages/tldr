# asciinema

> 터미널 세션을 녹화 및 재생하며, 선택적으로 <https://asciinema.org>에서 공유 가능.
> 관련 항목: `terminalizer`, `agg`.
> 더 많은 정보: <https://docs.asciinema.org/manual/cli/>.

- 로컬에 설치된 `asciinema`를 asciinema.org 계정과 연결:

`asciinema {{[a|auth]}}`

- 새로운 녹화를 시작하고 로컬 파일로 저장 (`<Ctrl d>`를 누르거나 `exit`을 입력하면 종료됨):

`asciinema {{[r|record]}} {{경로/대상/녹화파일.cast}}`

- 로컬 파일에 저장된 터미널 녹화를 재생:

`asciinema {{[p|play]}} {{경로/대상/녹화파일.cast}}`

- <https://asciinema.org>에 호스팅된 터미널 녹화를 재생:

`asciinema {{[p|play]}} https://asciinema.org/a/{{cast_id}}`

- 새로운 녹화를 시작하고, 유휴 시간을 최대 2.5초로 제한:

`asciinema {{[r|record]}} {{[-i|--idle-time-limit]}} 2.5`

- 로컬에 저장된 녹화 파일의 전체 출력을 표시:

`asciinema {{[ca|cat]}} {{경로/대상/녹화파일.cast}}`

- 로컬에 저장된 터미널 세션을 asciinema.org에 업로드:

`asciinema {{[u|upload]}} {{경로/대상/녹화파일.cast}}`

- 현재 터미널을 로컬 웹 페이지에서 스트리밍:

`asciinema {{[st|stream]}} --local`
