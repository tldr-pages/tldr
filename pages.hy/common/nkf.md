# nkf

> Ցանցային kanji ֆիլտր. փոխարկեք kanji կոդը մեկ կոդավորումից մյուսը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/nkf>:.

- Փոխարկել UTF-8 կոդավորմանը.:

`nkf -w {{path/to/file.txt}}`

- Փոխարկել SHIFT_JIS կոդավորման.:

`nkf -s {{path/to/file.txt}}`

- Փոխարկեք UTF-8 կոդավորման և վերագրեք ֆայլը.:

`nkf -w --overwrite {{path/to/file.txt}}`

- Օգտագործեք LF-ն որպես նոր տողի կոդ և վերագրեք (UNIX տիպ).:

`nkf -d --overwrite {{path/to/file.txt}}`

- Օգտագործեք CRLF-ը որպես նոր տողի կոդ և վերագրեք (պատուհանների տեսակը).:

`nkf -c --overwrite {{path/to/file.txt}}`

- Ապակոդավորեք mime ֆայլը և վերագրեք.:

`nkf -m --overwrite {{path/to/file.txt}}`
