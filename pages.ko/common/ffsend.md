# ffsend

> 쉽고 안전하게 파일을 공유.
> 더 많은 정보: <https://gitlab.com/timvisee/ffsend>.

- 파일 업로드:

`ffsend upload {{경로/대상/파일}}`

- 파일 다운로드:

`ffsend download {{url}}`

- 비밀번호가 포함된 파일 업로드:

`ffsend upload {{경로/대상/파일}} {{[-p|--password]}} {{비밀번호}}`

- 비밀번호로 보호된 파일 다운로드:

`ffsend download {{url}} {{[-p|--password]}} {{비밀번호}}`

- 파일을 업로드하고 4번의 다운로드를 허용:

`ffsend upload {{경로/대상/파일}} {{[-d|--downloads]}} {{4}}`
