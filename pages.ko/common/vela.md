# vela

> Vela 파이프라인을 위한 명령줄 도구.
> 더 많은 정보: <https://go-vela.github.io/docs/reference/cli>.

- Git 브랜치, 커밋 또는 태그에서 파이프라인 실행 트리거:

`vela add deployment --org {{조직}} --repo {{저장소_이름}} --target {{환경}} --ref {{브랜치|커밋|refs/tags/git_태그}} --description "{{배포_설명}}"`

- 저장소의 배포 목록 보기:

`vela get deployment --org {{조직}} --repo {{저장소_이름}}`

- 특정 배포 검사:

`vela view deployment --org {{조직}} --repo {{저장소_이름}} --deployment {{배포_번호}}`
