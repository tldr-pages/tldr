# ytmdl

> YouTube에서 노래를 다운로드하고 메타데이터를 자동으로 추가.
> iTunes, Spotify 등 소스에서 곡 정보를 가져옴 (아티스트, 앨범, 커버 아트).
> 더 많은 정보: <https://github.com/deepjyoti30/ytmdl#usage>.

- 곡 이름으로 노래를 다운로드 (대화형으로 결과 선택):

`ytmdl {{곡_이름}}`

- 사용자 입력 없이 첫 번째 검색 결과 다운로드:

`ytmdl {{[-q|--quiet]}} {{곡_이름}}`

- 지정한 디렉터리에 노래 다운로드:

`ytmdl {{[-o|--output-dir]}} {{경로/대상/디렉터리}} {{곡_이름}}`

- YouTube URL에서 노래 다운로드:

`ytmdl --url https://www.youtube.com/watch?v={{oHg5SJYRHA0}}`

- 지정한 형식으로 노래 다운로드 (mp3, m4a, opus):

`ytmdl --format {{mp3|m4a|opus}} {{곡_이름}}`

- 아티스트 및 앨범 정보를 지정하여 노래 다운로드:

`ytmdl --artist {{아티스트_이름}} --album {{앨범_이름}} {{곡_이름}}`

- 텍스트 파일에 있는 노래 목록 다운로드:

`ytmdl --list {{경로/대상/목록.txt}}`

- 도움말 표시:

`ytmdl {{[-h|--help]}}`
