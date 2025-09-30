# gitk

> Git 저장소를 그래픽으로 탐색.
> 참고: `git-gui`, `git-cola`, `tig`.
> 더 많은 정보: <https://git-scm.com/docs/gitk>.

- 현재 Git 저장소에 대한 저장소 브라우저를 표시:

`gitk`

- 특정 파일이나 디렉토리에 대한 저장소 브라우저 표시:

`gitk {{경로/대상/파일_또는_디렉토리}}`

- 1주일 전 이후에 이루어진 커밋 표시:

`gitk --since="{{1 week ago}}"`

- 2016년 1월 1일보다 오래된 커밋을 표시:

`gitk --until="{{1/1/2015}}"`

- 모든 지점에서 최대 100개의 변경 사항 표시:

`gitk --max-count=100 --all`
