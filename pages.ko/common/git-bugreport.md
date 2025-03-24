# git bugreport

> 시스템 및 사용자로부터 디버그 정보를 수집하여 Git 버그 보고에 도움이 되는 텍스트 파일을 생성합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-bugreport>.

- 현재 디렉토리에 새로운 버그 보고 파일 생성:

`git bugreport`

- 지정된 디렉토리에 새로운 버그 보고 파일 생성 (디렉토리가 없을 경우 생성됨):

`git bugreport {{[-o|--output-directory]}} {{경로/대상/폴더}}`

- `strftime` 형식의 지정된 파일명 접미사를 사용하여 새로운 버그 보고 파일 생성:

`git bugreport {{[-s|--suffix]}} {{%m%d%y}}`
