# rtmpdump

> Dump media content streamed over the RTMP protocol.
> More information: <https://rtmpdump.mplayerhq.hu/>.

- Download a file:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-o|--flv]}} {{file.ext}}`

- Download a file from a Flash player:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-W|--swfVfy]}} {{http://example.com/player}} {{[-f|--flashVer]}} "{{LNX 10,0,32,18}}" {{[-o|--flv]}} {{file.ext}}`

- Specify connection parameters if they are not detected correctly:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-a|--app]}} {{app_name}} {{[-y|--playpath]}} {{path/to/video}} {{[-o|--flv]}} {{file.ext}}`

- Download a file from a server that requires a referrer:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-p|--pageUrl]}} {{http://example.com/webpage}} {{[-o|--flv]}} {{file.ext}}`
