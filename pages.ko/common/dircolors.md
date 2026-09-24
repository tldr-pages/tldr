# dircolors

> `$LS_COLOR` 환경 변수를 설정하고, `ls`, `dir` 등의 출력 색상을 지정하기 위한 명령을 출력.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>.

- 기본 색상 설정을 사용하여 `$LS_COLOR`를 설정하는 명령 출력:

`dircolors`

- `ls`에서 각 파일 유형이 어떤 색으로 표시되는지 출력:

`dircolors --print-ls-colors`

- 특정 파일에 정의된 색상 설정을 사용해 `$LS_COLOR`를 설정하는 명령 출력:

`dircolors {{경로/대상/파일}}`

- Bourne 쉘용 명령 출력:

`dircolors {{[-b|--bourne-shell]}}`

- C 쉘용 명령 출력:

`dircolors {{[-c|--c-shell]}}`

- 파일 유형 및 확장자에 대한 기본 색상 설정 보기:

`dircolors {{[-p|--print-database]}}`
