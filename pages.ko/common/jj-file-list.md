# jj file list

> `jj` 저장소의 리비전 내 파일 목록 표시.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-list>.

- 현재 작업 복사본 모든 파일 목록 표시:

`jj file list`

- 지정한 리비전 모든 파일의 목록 표시:

`jj file list {{[-r|--revision]}} {{리비전}}`

- 지정한 접두사 또는 경로와 일치하는 파일 목록 표시:

`jj file list {{경로/대상/디렉터리}}`

- 사용자 지정 템플릿을 사용해 파일 목록 표시:

`jj file list {{[-T|--template]}} "{{템플릿}}"`
