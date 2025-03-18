# pkgctl repo

> Arch Linux용 Git 패키징 저장소 및 구성 관리.
> 같이 보기: `pkgctl`.
> 더 많은 정보: <https://manned.org/pkgctl-repo.1>.

- 패키지 저장소를 클론(Arch Linux GitLab 계정에 SSH 키 설정 필요):

`pkgctl repo clone {{패키지명}}`

- HTTPS를 통해 패키지 저장소를 클론:

`pkgctl repo clone --protocol https {{패키지명}}`

- 새로운 GitLab 패키지 저장소 생성 후 클론(GitLab API 인증 필요):

`pkgctl repo create {{패키지_기본명}}`

- 특정 버전으로 패키지 저장소 전환:

`pkgctl repo switch {{버전}} {{패키지_기본명}}`

- 패키지 저장소의 웹사이트 열기:

`pkgctl repo web {{패키지_기본명}}`
