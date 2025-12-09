# youtube-dl

> YouTube 및 다른 웹사이트에서 비디오를 다운로드.
> 같이 보기: `yt-dlp`, `ytfzf`, `you-get`.
> 더 많은 정보: <https://rg3.github.io/youtube-dl/>.

- 비디오 또는 재생 목록 다운로드:

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- 비디오 또는 재생 목록이 가능한 모든 형식 나열:

`youtube-dl --list-formats '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- 특정 품질로 비디오 또는 재생 목록 다운로드:

`youtube-dl --format "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- 비디오에서 오디오만 다운로드하고 MP3로 변환:

`youtube-dl -x --audio-format {{mp3}} '{{url}}'`

- 최고 품질의 오디오와 비디오를 다운로드하고 병합:

`youtube-dl -f bestvideo+bestaudio '{{url}}'`

- 맞춤 파일 이름으로 MP4 파일로 비디오 다운로드:

`youtube-dl --format {{mp4}} -o "{{%(playlist_index)s-%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s}}" '{{url}}'`

- 특정 언어의 자막을 비디오와 함께 다운로드:

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- 재생 목록을 다운로드하고 MP3로 추출:

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" '{{url_to_playlist}}'`
