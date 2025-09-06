# git secret

> Git 리포지토리에 개인 데이터를 저장. Bash로 작성됨.
> 더 많은 정보: <https://github.com/sobolevn/git-secret>.

- 로컬 리포지토리에 `git-secret` 초기화:

`git secret init`

- 현재 Git 사용자의 이메일에 액세스 권한 부여:

`git secret tell -m`

- 이메일로 액세스 권한 부여:

`git secret tell {{email}}`

- 이메일로 액세스 권한 취소:

`git secret killperson {{email}}`

- 비밀에 대한 액세스 권한이 있는 이메일 목록:

`git secret whoknows`

- 비밀 파일 등록:

`git secret add {{경로/대상/파일}}`

- 비밀 암호화:

`git secret hide`

- 비밀 파일 복호화:

`git secret reveal`
