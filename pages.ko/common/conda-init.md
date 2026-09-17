# conda init

> 쉘에서 conda를 사용할 수 있도록 초기화.
> 대부분 쉘은 변경 사항이 적용되려면, 종료 후 다시 시작해야 합니다.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/init.html>.

- 특정 쉘 초기화 (지정하지 않으면, UNIX는 `bash`,  Windows는 `powershell` 기본 사용):

`conda init {{zsh|bash|powershell|fish|tcsh|xonsh}}`

- 사용 가능한 모든 쉘 초기화:

`conda init --all`

- 시스템의 모든 사용자를 대상으로 conda 초기화:

`conda init --system`

- 현재 사용자에 대해서는 conda를 초기화하지 않음:

`conda init --no-user`

- `condabin/` 디렉터리를 `$PATH`에 추가:

`conda init --condabin`

- 마지막 `conda init` 실행의 변경 사항 되돌리기:

`conda init --reverse`
