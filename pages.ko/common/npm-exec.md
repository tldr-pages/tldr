# npm exec

> `npm` 패키지 바이너리 실행.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-exec/>.

- 로컬 또는 원격 `npm` 패키지 명령어 실행:

`npm {{[x|exec]}} {{명령어}} {{argument1 argument2 ...}}`

- 특정 패키지를 명시하여 실행 (동일한 이름의 명령이 여러개 있을 때 유용):

`npm {{[x|exec]}} --package {{패키지}} {{명령어}}`

- `node_modules/.bin`에 존재하는 경우에만 실행:

`npm {{[x|exec]}} --no-install {{명령어}} {{인자1 인자2 ...}}`

- `npm` 자체 출력 없이 명령 실행:

`npm {{[x|exec]}} --quiet {{명령어}} {{인자1 인자2 ...}}`

- 도움말 표시:

`npm {{[x|exec]}} --help`
