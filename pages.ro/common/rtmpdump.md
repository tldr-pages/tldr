# rtmpdump

> Un instrument pentru a arunca conținut media redat în flux prin protocolul RTMP.
> Mai multe informaţii: <http://rtmpdump.mplayerhq.hu/>

- Descărcați un fișier:

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} -o {{file.ext}}`

- Descărcați un fișier de la un player Flash:

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --swfVfy {{http://example.com/player}} --flashVer "{{LNX 10,0,32,18}}" -o {{file.ext}}`

- Specificați parametrii conexiunii dacă nu sunt detectați corect:

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --app {{app_name}} --playpath {{path/to/video}} -o {{file.ext}}`

- Descărcați un fișier de pe un server care necesită un referrer:

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --pageUrl {{http://example.com/webpage}} -o {{file.ext}}`
