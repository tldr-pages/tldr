# gst-launch-1.0 playbin

> Standalone media player.
> More information: <https://gstreamer.freedesktop.org/documentation/playback/playbin.html>.

- 로컬 파일 재생:

`gst-launch-1.0 playbin uri=file:///{{경로/대상/파일}}`

- 인터넷의 파일 재생:

`gst-launch-1.0 playbin uri={{https://example.com/경로/대상/파일}}`

- CD의 4번 트랙 재생:

`gst-launch-1.0 playbin uri=cdda://4`

- 디스크 드라이브의 DVD 재생:

`gst-launch-1.0 playbin uri=dvd://`
