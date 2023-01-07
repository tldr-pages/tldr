# git clean

> 워킹 트리에서 추적되지 않는 파일을 제거합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-clean>.

- 깃에 의해 추적되지 않는 파일들 지우기:

`git clean`

- 깃에 의해 추적되지 않는 파일들 인터액티브 하게 지우기:

`git clean -i`

- 어떤 파일들이 제거될 것인지 실제로 지우지 않고 보여주기:

`git clean --dry-run`

- 깃에 의해 추적되지 않는 파일들 강제적으로 지우기:

`git clean -f`

- 깃에 의해 추적되지 않는 디렉토리를 강제적으로 지우기:

`git clean -fd`

- 추적되지 않는 파일들, `.gitignore` 와 `.git/info/exclude` 안에 있는 무시된 파일들을 포함하여 지우기:

`git clean -x`
