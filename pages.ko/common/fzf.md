# fzf

> 명령줄 퍼지 찾기.
> `sk`와 유사.
> 더 많은 정보: <https://github.com/junegunn/fzf#usage>.

- 지정된 디렉터리의 모든 파일에서 `fzf`를 시작:

`find {{경로/대상/디렉터리}} -type f | fzf`

- 프로세스 실행을 위해 `fzf`를 시작:

`ps aux | fzf`

- `<Shift Tab>`을 사용해 여러 파일을 선택하고 파일에 작성:

`find {{경로/대상/디렉터리}} -type f | fzf {{[-m|--multi]}} > {{경로/대상/파일}}`

- 지정된 쿼리로 `fzf`를 시작:

`fzf {{[-q|--query]}} "{{쿼리}}"`

- core로 시작하고 go, rb 또는 py로 끝나는 항목에서 `fzf`를 시작:

`fzf {{[-q|--query]}} "^core go$ | rb$ | py$"`

- pvc와 일치하지 않고 travis와 정확히 일치하는 항목에 대해 `fzf`를 시작:

`fzf {{[-q|--query]}} "!pyc 'travis"`
