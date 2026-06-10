# hlsq

> Ցուցադրել HLS-ի դրսևորումները գունավոր և հիմնական զտիչով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/soldiermoth/hlsq/>:.

- Դիտեք HLS մանիֆեստը URL-ից.:

`{{curl --silent url}} | hlsq`

- Դիտեք HLS մանիֆեստը ֆայլից.:

`{{cat path/to/file.m3u8}} | hlsq`

- Անընդհատ վերբեռնեք URL-ը և թարմացրեք ելքը.:

`hlsq -watch -url {{url}}`

- Զտել բազմատեսակ երգացանկը ըստ հատկանիշի լարային արժեքի.:

`{{cat path/to/file.m3u8}} | hlsq -query '{{type = SUBTITLES}}'`

- Զտել բազմատեսակ երգացանկը ըստ հատկանիշի թվային արժեքի.:

`{{cat path/to/file.m3u8}} | hlsq -query '{{bandwidth > 1000000}}'`
