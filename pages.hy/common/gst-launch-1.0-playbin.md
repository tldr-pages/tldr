# gst-launch-1.0 նվագարկիչ

> Անկախ մեդիա նվագարկիչ:.
> Լրացուցիչ տեղեկություններ. <https://gstreamer.freedesktop.org/documentation/playback/playbin.html>:.

- Խաղացեք տեղական ֆայլ.:

`gst-launch-1.0 playbin uri=file:///{{path/to/file}}`

- Ֆայլ խաղալ ինտերնետից.:

`gst-launch-1.0 playbin uri={{https://example.com/path/to/file}}`

- Նվագարկել ձայնասկավառակի 4-րդ կատարումը.:

`gst-launch-1.0 playbin uri=cdda://4`

- Նվագարկել DVD սկավառակ սկավառակի մեջ.:

`gst-launch-1.0 playbin uri=dvd://`
