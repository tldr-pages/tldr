# equery

> Portage 패키지에 대한 정보를 표시합니다.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Equery>.

- 설치된 모든 패키지 나열:

`equery list '*'`

- 포티지 트리와 오버레이에서 설치된 패키지를 검색:

`equery list -po {{패키지1 패키지2 ...}}`

- 특정 패키지에 의존하는 모든 패키지 나열:

`equery depends {{패키지}}`

- 특정 패키지가 의존하는 모든 패키지 나열:

`equery depgraph {{패키지}}`

- 패키지가 설치한 모든 파일 나열:

`equery files --tree {{패키지}}`
