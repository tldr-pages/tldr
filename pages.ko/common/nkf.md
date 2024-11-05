# nkf

> 네트워크 한자 필터: 한자 코드를 하나의 인코딩에서 다른 인코딩으로 변환.
> 더 많은 정보: <https://manned.org/nkf>.

- UTF-8 인코딩으로 변환:

`nkf -w {{경로/대상/파일.txt}}`

- SHIFT_JIS 인코딩으로 변환:

`nkf -s {{경로/대상/파일.txt}}`

- UTF-8 인코딩으로 변환하고 파일 덮어쓰기:

`nkf -w --overwrite {{경로/대상/파일.txt}}`

- LF를 새 줄 코드로 사용하고 덮어쓰기 (UNIX 타입):

`nkf -d --overwrite {{경로/대상/파일.txt}}`

- CRLF를 새 줄 코드로 사용하고 덮어쓰기 (Windows 타입):

`nkf -c --overwrite {{경로/대상/파일.txt}}`

- MIME 파일을 해독하고 덮어쓰기:

`nkf -m --overwrite {{경로/대상/파일.txt}}`
