# mac2unix

> macOS 스타일의 줄 바꿈을 Unix 스타일로 변경.
> CR을 LF로 대체.
> 같이 보기: `unix2dos`, `unix2mac`, `dos2unix`.
> 더 많은 정보: <https://manned.org/mac2unix>.

- 파일의 줄 바꿈 변경:

`mac2unix {{경로/대상/파일}}`

- Unix 스타일의 줄 바꿈을 가진 파일 복사본 생성:

`mac2unix {{[-n|--newfile]}} {{경로/대상/파일}} {{경로/대상/새_파일}}`

- 파일 정보 표시:

`mac2unix {{[-i|--info]}} {{경로/대상/파일}}`

- 바이트 순서 표시(BOM) 유지/추가/제거:

`mac2unix --{{keep-bom|add-bom|remove-bom}} {{경로/대상/파일}}`
