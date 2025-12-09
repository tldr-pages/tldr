# gh gist

> GitHub Gist 작업.
> 더 많은 정보: <https://cli.github.com/manual/gh_gist>.

- 하나 이상의 파일에서 새 Gist 생성:

`gh gist create {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 특정 설명으로 새 Gist 생성:

`gh gist create {{경로/대상/파일1 경로/대상/파일2 ...}} --desc "{{설명}}"`

- Gist 수정:

`gh gist edit {{id|url}}`

- 현재 로그인된 사용자가 소유한 최대 42개의 Gist 나열:

`gh gist list --limit {{42}}`

- 기본 브라우저에서 마크다운 렌더링 없이 Gist 보기:

`gh gist view {{id|url}} --web --raw`
