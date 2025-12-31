# yt-dlp

> 추가 기능과 수정이 포함된 youtube-dl 포크.
> YouTube 및 기타 웹사이트에서 동영상을 다운로드합니다.
> 같이 보기: `yt-dlp`, `ytfzf`.
> 더 많은 정보: <https://github.com/yt-dlp/yt-dlp#usage-and-options>.

- 동영상 또는 재생목록 다운로드 (아래 명령의 기본 옵션 사용):

`yt-dlp "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- 동영상의 다운로드 가능한 형식 나열:

`yt-dlp --list-formats "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- 사용 가능한 최고의 MP4 비디오로 동영상 또는 재생목록 다운로드 (기본은 "bv*+ba/b"):

`yt-dlp --format "{{bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]}}" "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- 동영상에서 오디오 추출 (ffmpeg 또는 ffprobe 필요):

`yt-dlp --extract-audio "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- 추출된 오디오의 형식과 품질 지정 (0 (최고)에서 10 (최악) 사이, 기본값 = 5):

`yt-dlp --extract-audio --audio-format {{mp3}} --audio-quality {{0}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- YouTube 채널/사용자의 모든 재생목록을 각각의 폴더에 저장하여 다운로드:

`yt-dlp -o "{{%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s}}" "{{https://www.youtube.com/user/TheLinuxFoundation/playlists}}"`

- Udemy 강의를 각 챕터별로 다른 폴더에 저장하여 다운로드:

`yt-dlp -u {{사용자}} -p {{비밀번호}} -P "{{경로/대상/폴더}}" -o "{{%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s}}" "{{https://www.udemy.com/java-tutorial}}"`
