# megatools-dl

> `mega.nz`에서 파일을 다운로드.
> `megatools` 모음의 일부.
> 더 많은 정보: <https://megatools.megous.com/man/megatools-dl.html>.

- `mega.nz` 링크에서 현재 디렉터리로 파일 다운로드:

`megatools-dl {{https://mega.nz/...}}`

- `mega.nz` 링크에서 특정 디렉터리로 파일 다운로드:

`megatools-dl --path {{경로/대상/폴더}} {{https://mega.nz/...}}`

- 다운로드할 파일을 대화형으로 선택:

`megatools-dl --choose-files {{https://mega.nz/...}}`

- 다운로드 속도를 KiB/s 단위로 제한:

`megatools-dl --limit-speed {{속도}} {{https://mega.nz/...}}`
