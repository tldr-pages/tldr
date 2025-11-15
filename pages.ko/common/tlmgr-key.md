# tlmgr key

> TeX Live 데이터베이스를 검증하는 데 사용되는 GPG 키 관리.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#key>.

- TeX Live의 모든 키 나열:

`tlmgr key list`

- 특정 파일에서 키 추가:

`sudo tlmgr key add {{경로/대상/키.gpg}}`

- `stdin`에서 키 추가:

`cat {{경로/대상/키.gpg}} | sudo tlmgr key add -`

- ID로 특정 키 제거:

`sudo tlmgr key remove {{키_ID}}`
