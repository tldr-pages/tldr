# popd

> `pushd` 셸 내장 명령어를 통해 디렉토리 스택에 올려놓은 디렉토리를 제거.
> `pushd`로 스택에 디렉토리를 올리는 방법과 `dirs`로 디렉토리 스택 내용을 표시하는 방법도 참고.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html#index-popd>.

- 스택의 최상위 디렉토리를 제거하고 해당 디렉토리로 이동:

`popd`

- N번째 디렉토리 제거 (왼쪽에서 0부터 시작, `dirs`로 출력된 목록 기준):

`popd +N`

- N번째 디렉토리 제거 (오른쪽에서 0부터 시작, `dirs`로 출력된 목록 기준):

`popd -N`

- 첫 번째 디렉토리 제거 (왼쪽에서 0부터 시작, `dirs`로 출력된 목록 기준):

`popd -n`
