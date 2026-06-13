# paperkey

> OpenPGP 키 아카이버.
> 더 많은 정보: <https://www.jabberwocky.com/software/paperkey/>.

- 특정 비밀 키를 가져와 비밀 데이터를 포함한 텍스트 파일 생성:

`paperkey --secret-key {{경로/대상/비밀_키.gpg}} --output {{경로/대상/비밀_데이터.txt}}`

- `secret_data.txt`에 있는 비밀 키 데이터를 가져와 공개 키와 결합하여 비밀 키 재구성:

`paperkey --pubring {{경로/대상/공개_키.gpg}} --secrets {{경로/대상/비밀_데이터.txt}} --output {{비밀_키.gpg}}`

- 특정 비밀 키를 내보내고 비밀 데이터를 포함한 텍스트 파일 생성:

`gpg --export-secret-key {{키}} | paperkey --output {{경로/대상/비밀_데이터.txt}}`
