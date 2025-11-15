# gh secret set

> GitHub 시크릿 생성 또는 업데이트.
> 더 많은 정보: <https://cli.github.com/manual/gh_secret_set>.

- 현재 저장소에 시크릿 설정 (사용자에게 값 입력을 요청함):

`gh secret set {{이름}}`

- 파일에서 값을 읽어와 현재 저장소에 시크릿 설정:

`gh secret set {{이름}} < {{경로/대상/파일}}`

- 특정 저장소에 시크릿 설정:

`gh secret set {{이름}} --body {{값}} --repo {{소유자}}/{{저장소}}`

- 특정 저장소들에 대해 조직 시크릿 설정:

`gh secret set {{이름}} --org {{조직}} --repos "{{저장소1,저장소2,...}}"`

- 특정 가시성으로 조직 시크릿 설정:

`gh secret set {{이름}} --org {{조직}} --visibility {{all|private|selected}}`
