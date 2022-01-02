# yt-dlp

> A youtube-dl fork with additional features and fixes.
> Download videos from YouTube and other websites.
> More information: <https://github.com/yt-dlp/yt-dlp>.

- Download a video or playlist (with the default options from command below):
`yt-dlp "https://www.youtube.com/watch?v=oHg5SJYRHA0"`

- Download best format that contains video, and if it doesn't already have an audio stream, merge it with best audio-only format (Default)
`yt-dlp -f "bv*+ba/b "https://www.youtube.com/watch?v=oHg5SJYRHA0"`

- Download YouTube playlist videos in separate directory indexed by video order in a playlist
`yt-dlp -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re"`

- Download YouTube playlist videos in separate directories according to their uploaded year
`yt-dlp -o "%(upload_date>%Y)s/%(title)s.%(ext)s" "https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re"`

- Download all playlists of YouTube channel/user keeping each playlist in separate directory:
`yt-dlp -o "%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "https://www.youtube.com/user/TheLinuxFoundation/playlists"`

- Download Udemy course keeping each chapter in separate directory under MyVideos directory in your home
`yt-dlp -u user -p password -P "~/MyVideos" -o "%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s" "https://www.udemy.com/java-tutorial"`

- Download entire series season keeping each series and each season in separate directory under C:/MyVideos
`yt-dlp -P "C:/MyVideos" -o "%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s" "https://videomore.ru/kino_v_detalayah/5_sezon/367617"`


