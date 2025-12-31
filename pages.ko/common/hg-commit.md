# hg commit

> 준비된 모든 파일 또는 지정된 파일을 저장소에 커밋.
> 더 많은 정보: <https://www.mercurial-scm.org/help/commands/commit>.

- 준비된 파일을 저장소에 커밋:

`hg commit`

- 특정 파일 또는 디렉터리를 커밋:

`hg commit {{경로/대상/파일_또는_디렉터리}}`

- 특정 메시지와 함께 커밋:

`hg commit --message {{메시지}}`

- 지정된 패턴과 일치하는 모든 파일을 커밋:

`hg commit --include {{패턴}}`

- 지정된 패턴과 일치하지 않는 모든 파일을 커밋:

`hg commit --exclude {{패턴}}`

- 대화형 모드를 사용하여 커밋:

`hg commit --interactive`
