# rtmpdump

> A tool to dump media content streamed over the RTMP protocol.
> More information: <http://rtmpdump.mplayerhq.hu/>.

- Download a file:

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} -o {{file.ext}}`

- Download a file that requires specific connection parameters:

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --app {{app_name}} --pageUrl {{http://example.com/webpage}} --swfVfy {{http://example.com/player}} --flashVer {{LNX 10,0,32,18}} --playpath {{playpath}} -o {{file.ext}}`
