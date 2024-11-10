# protector

> GitHub 저장소의 브랜치를 보호하거나 보호 해제.
> 더 많은 정보: <https://github.com/jcgay/protector>.

- GitHub 저장소의 브랜치 보호 (브랜치 보호 규칙 생성):

`protector {{브랜치_정규식}} -repos {{조직/저장소}}`

- 보호될 브랜치 미리보기 (해제에도 사용 가능):

`protector -dry-run {{브랜치_정규식}} -repos {{조직/저장소}}`

- GitHub 저장소의 브랜치 보호 해제 (브랜치 보호 규칙 삭제):

`protector -free {{브랜치_정규식}} -repos {{조직/저장소}}`
