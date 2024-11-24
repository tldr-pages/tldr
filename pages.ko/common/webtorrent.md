# webtorrent

> WebTorrent의 명령줄 인터페이스.
> 마그넷, URL, 정보 해시 및 `.torrent` 파일을 지원.
> 더 많은 정보: <https://github.com/webtorrent/webtorrent-cli>.

- 토렌트 다운로드:

`webtorrent download "{{토렌트_id}}"`

- VLC 미디어 플레이어로 토렌트 스트리밍:

`webtorrent download "{{토렌트_id}}" --vlc`

- DLNA (Digital Living Network Alliance) 장치로 토렌트 스트리밍:

`webtorrent download "{{토렌트_id}}" --dlna`

- 특정 토렌트의 파일 목록 표시:

`webtorrent download "{{토렌트_id}}" --select`

- 다운로드할 토렌트에서 파일 색인 지정:

`webtorrent download "{{토렌트_id}}" --select {{색인}}`

- 특정 파일 또는 폴더 시드:

`webtorrent seed {{경로/대상/파일_또는_폴더}}`

- 지정된 파일 경로에 대한 새 토렌트 파일 생성:

`webtorrent create {{경로/대상/파일}}`

- 마그넷 URI 또는 `.torrent` 파일에 대한 정보 표시:

`webtorrent info {{경로/대상/파일_또는_마그넷}}`
