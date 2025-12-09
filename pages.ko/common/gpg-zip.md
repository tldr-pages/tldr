# gpg-zip

> GPG를 사용하여 아카이브의 파일과 디렉터리를 암호화.
> 더 많은 정보: <https://www.gnupg.org/documentation/manuals/gnupg/gpg_002dzip.html>.

- 비밀번호 문구를 사용하여 디렉터리를 `archive.gpg`로 암호화:

`gpg-zip --symmetric --output {{아카이브.gpg}} {{경로/대상/디렉터리}}`

- `아카이브.gpg`를 같은 이름의 디렉터리로 복호화:

`gpg-zip --decrypt {{경로/대상/아카이브.gpg}}`

- 암호화된 `아카이브.gpg`의 내용을 나열:

`gpg-zip --list-archive {{경로/대상/아카이브.gpg}}`
