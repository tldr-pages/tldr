# ytfzf

> 비디오 및 음악을 찾고 다운로드. POSIX 셸로 작성되었습니다.
> 같이 보기: `youtube-dl`, `yt-dlp`, `instaloader`.
> 더 많은 정보: <https://manned.org/ytfzf>.

- YouTube에서 썸네일 미리보기로 비디오 검색:

`ytfzf --show-thumbnails {{검색_패턴}}`

- 첫 번째 항목의 오디오만 반복 재생:

`ytfzf --audio-only --auto-select --loop {{검색_패턴}}`

- 기록에서 비디오 다운로드:

`ytfzf --download --choose-from-history`

- 검색에서 찾은 모든 음악 재생:

`ytfzf --audio-only --select-all {{검색_패턴}}`

- 외부 메뉴에서 인기 비디오 보기:

`ytfzf --trending --ext-menu {{검색_패턴}}`

- YouTube 대신 PeerTube에서 검색:

`ytfzf --peertube {{검색_패턴}}`
