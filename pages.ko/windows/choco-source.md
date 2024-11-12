# choco source

> Chocolatey 패키지 소스 관리.
> 더 많은 정보: <https://chocolatey.org/docs/commands-source>.

- 현재 사용 가능한 소스 나열:

`choco source list`

- 새 패키지 소스 추가:

`choco source add --name {{이름}} --source {{url}}`

- 자격 증명을 사용하여 새 패키지 소스 추가:

`choco source add --name {{이름}} --source {{url}} --user {{사용자_명}} --password {{비밀번호}}`

- 클라이언트 인증서를 사용하여 새 패키지 소스 추가:

`choco source add --name {{이름}} --source {{url}} --cert {{경로\대상\인증서_파일}}`

- 패키지 소스 활성화:

`choco source enable --name {{이름}}`

- 패키지 소스 비활성화:

`choco source disable --name {{이름}}`

- 패키지 소스 제거:

`choco source remove --name {{이름}}`
