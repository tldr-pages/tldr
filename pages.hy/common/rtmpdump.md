# rtmpdump

> Թափել մեդիա բովանդակությունը, որը հեռարձակվում է RTMP արձանագրությամբ:.
> Լրացուցիչ տեղեկություններ. <https://rtmpdump.mplayerhq.hu/rtmpdump.1.html>:.

- Ներբեռնեք ֆայլ.:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-o|--flv]}} {{file.ext}}`

- Ներբեռնեք ֆայլ Flash նվագարկիչից.:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-W|--swfVfy]}} {{http://example.com/player}} {{[-f|--flashVer]}} "{{LNX 10,0,32,18}}" {{[-o|--flv]}} {{file.ext}}`

- Նշեք կապի պարամետրերը, եթե դրանք ճիշտ չեն հայտնաբերվել.:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-a|--app]}} {{app_name}} {{[-y|--playpath]}} {{path/to/video}} {{[-o|--flv]}} {{file.ext}}`

- Ներբեռնեք ֆայլ սերվերից, որը հղում է պահանջում.:

`rtmpdump {{[-r|--rtmp]}} {{rtmp://example.com/path/to/video}} {{[-p|--pageUrl]}} {{http://example.com/webpage}} {{[-o|--flv]}} {{file.ext}}`
