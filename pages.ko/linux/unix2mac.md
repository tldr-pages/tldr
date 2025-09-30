# unix2mac

> Unix 스타일의 줄 끝을 macOS 스타일로 변경.
> LF를 CR로 대체.
> 같이 보기: `unix2dos`, `dos2unix`, `mac2unix`.
> 더 많은 정보: <https://manned.org/unix2mac>.

- 파일의 줄 끝을 변경:

`unix2mac {{경로/대상/파일}}`

- macOS 스타일의 줄 끝을 가진 복사본 생성:

`unix2mac {{[-n|--newfile]}} {{경로/대상/파일}} {{경로/대상/새_파일}}`

- 파일 정보 표시:

`unix2mac {{[-i|--info]}} {{경로/대상/파일}}`

- 바이트 순서 표식 유지/추가/제거:

`unix2mac --{{keep-bom|add-bom|remove-bom}} {{경로/대상/파일}}`
