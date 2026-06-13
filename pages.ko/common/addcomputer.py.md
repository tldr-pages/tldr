# addcomputer.py

> 도메인에 컴퓨터 계정을 추가하는 도구.
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 특정 이름과 비밀번호로 컴퓨터 계정 추가:

`addcomputer.py -computer-name {{컴퓨터_이름$}} -computer-pass {{컴퓨터_비밀번호}} {{도메인}}/{{사용자명}}:{{비밀번호}}`

- 기존 컴퓨터 계정의 비밀번호만 변경:

`addcomputer.py -no-add -computer-name {{컴퓨터_이름$}} -computer-pass {{컴퓨터_비밀번호}} {{도메인}}/{{사용자명}}:{{비밀번호}}`

- 기존 컴퓨터 계정 삭제:

`addcomputer.py -delete -computer-name {{컴퓨터_이름$}} {{도메인}}/{{사용자명}}:{{비밀번호}}`

- Kerberos 인증을 사용하여 컴퓨터 추가:

`addcomputer.py -k -no-pass {{도메인}}/{{사용자명}}@{{호스트명}}`

- SAMR (포트 445) 대신 LDAPS (포트 636)를 사용하여 추가:

`addcomputer.py -method LDAPS -port 636 {{도메인}}/{{사용자명}}:{{비밀번호}}`

- 여러 도메인 컨트롤러 존재 시 특정 DC 지정:

`addcomputer.py -dc-host {{호스트명}} {{도메인}}/{{사용자명}}:{{비밀번호}}`
