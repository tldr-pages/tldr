# pushd

> 디렉터리를 스택에 쌓아 나중에 접근할 수 있도록 합니다.
> 원래 디렉터리로 돌아가려면 `popd`, 디렉터리 스택 내용을 보려면 `dirs`를 같이 보세요.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- 디렉터리로 이동하고 스택에 추가:

`pushd {{경로/대상/폴더}}`

- 스택의 첫 번째와 두 번째 디렉터리를 전환:

`pushd`

- 스택을 회전하여 5번째 요소를 스택의 맨 위로:

`pushd +4`

- 스택을 왼쪽으로 4번 회전 (현재 디렉터리는 5번째 요소를 교체하여 맨 위에 유지):

`pushd -n +4`
