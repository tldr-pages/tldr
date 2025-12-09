# certutil

> 인증서 정보를 관리하고 구성하는 도구.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/certutil>.

- 구성 정보 또는 파일 덤프:

`certutil {{파일_이름}}`

- 파일을 16진수로 인코딩:

`certutil -encodehex {{경로\대상\입력_파일}} {{경로\대상\출력_파일}}`

- 파일을 Base64로 인코딩:

`certutil -encode {{경로\대상\입력_파일}} {{경로\대상\출력_파일}}`

- Base64로 인코딩된 파일을 디코딩:

`certutil -decode {{경로\대상\입력_파일}} {{경로\대상\출력_파일}}`

- 파일에 대한 암호화 해시 생성 및 표시:

`certutil -hashfile {{경로\대상\입력_파일}} {{md2|md4|md5|sha1|sha256|sha384|sha512}}`
