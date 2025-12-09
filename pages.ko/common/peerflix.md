# peerflix

> 비디오 또는 오디오 기반 토렌트를 미디어 플레이어로 스트리밍.
> 더 많은 정보: <https://github.com/mafintosh/peerflix>.

- 토렌트에서 가장 큰 미디어 파일 스트리밍:

`peerflix "{{토렌트_URL|마그넷_링크}}"`

- 마그넷 링크로 주어진 토렌트에 포함된 모든 스트리밍 가능한 파일 나열:

`peerflix "{{magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567}}" --list`

- 토렌트 URL로 주어진 토렌트에서 가장 큰 파일을 VLC로 스트리밍:

`peerflix "{{http://example.net/music.torrent}}" --vlc`

- 자막과 함께 토렌트에서 가장 큰 파일을 MPlayer로 스트리밍:

`peerflix "{{토렌트_URL|마그넷_링크}}" --mplayer --subtitles {{자막_파일.srt}}`

- 토렌트의 모든 파일을 Airplay로 스트리밍:

`peerflix "{{토렌트_URL|마그넷_링크}}" --all --airplay`
