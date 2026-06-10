# picocom

> Սերիական կոնսուլները ընդօրինակելու նվազագույն ծրագիր:.
> Տես նաև՝ `minicom`, `cu`, `tio`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/picocom>:.

- Միացեք սերիական կոնսոլին 9600 լռելյայն baud արագությամբ:

`sudo picocom {{/dev/ttyXYZ}}`

- Միացեք սերիական կոնսոլին՝ սահմանված բուդ արագությամբ.:

`sudo picocom {{/dev/ttyXYZ}} {{[-b|--baud]}} {{baud_rate}}`

- Քարտեզագրեք հատուկ նիշերը (օրինակ՝ `LF`-ից `CRLF`):

`sudo picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`

- Ելք picocom:

`<Ctrl a><Ctrl x>`

- Ցուցադրել օգնությունը.:

`picocom {{[-h|--help]}}`
