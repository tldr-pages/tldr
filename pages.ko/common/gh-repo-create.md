# gh repo create

> 새로운 GitHub 저장소 생성.
> 참고: `--public`, `--private`, `--internal` 중 하나를 반드시 지정해야 함.
> 더 많은 정보: <https://cli.github.com/manual/gh_repo_create>.

- 새로운 저장소를 대화형으로 생성:

`gh repo {{[new|create]}}`

- 현재 디렉터리로부터 비공개 저장소 생성:

`gh repo {{[new|create]}} {{[-s|--source]}} . --private`

- 현재 디렉터리로부터 공개 저장소 생성:

`gh repo {{[new|create]}} {{[-s|--source]}} . --public`

- 이름과 설명을 지정하여 공개 저장소 생성:

`gh repo {{[new|create]}} {{저장소_이름}} {{[-d|--description]}} "{{저장소_설명}}" --public`

- 저장소 생성 후 로컬로 clone 수행:

`gh repo {{[new|create]}} {{저장소_이름}} {{[-c|--clone]}} {{--public|--private|--internal}}`
