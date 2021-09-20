# deluge-console

> Deluge BitTorrent 클라이언트를 위한 대화형 인터페이스.
> 더 많은 정보: <https://deluge-torrent.org>.

- 대화형 콘솔 인터페이스 시작:

`deluge-console`

- Deluge 데몬 객체에 연결:

`connect {{호스트이름}}:{{포트번호}}`

- 데몬에 토렌트 추가:

`add {{url|magnet|파일/경로}}`

- 모든 토렌트에 대한 정보 표시:

`info`

- 특정 토렌트에 대한 정보 표시:

`info {{토렌트_아이디}}`

- 토렌트 일시정지:

`pause {{토렌트_아이디}}`

- 토렌트 재시작:

`resume {{토렌트_아이디}}`

- 데몬으로부터 토렌트 제거:

`rm {{토렌트_아이디}}`
