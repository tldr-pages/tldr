# az disk

> Azure 관리 디스크를 관리.
> `azure-cli`의 일부(`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/disk>.

- 관리 디스크 만들기:

`az disk create {{[-g|--resource-group]}} {{리소스_그룹}} {{[-n|--name]}} {{디스크_이름}} {{[-z|--size-gb]}} {{기가바이트_크기}}`

- 리소스 그룹의 관리 디스크 나열:

`az disk list {{[-g|--resource-group]}} {{리소스_그룹}}`

- 관리 디스크 삭제:

`az disk delete {{[-g|--resource-group]}} {{리소스_그룹}} {{[-n|--name]}} {{디스크_이름}}`

- 관리 디스크에 대한 읽기 또는 쓰기 액세스 권한 부여 (내보내기 용):

`az disk grant-access {{[-g|--resource-group]}} {{리소스_그룹}} {{[-n|--name]}} {{디스크_이름}} {{[--access|--access-level]}} {{Read|Write}} --duration-in-seconds {{초}}`

- 디스크 사이즈 업데이트:

`az disk update {{[-g|--resource-group]}} {{리소스_그룹}} {{[-n|--name]}} {{디스크_이름}} {{[-z|--size-gb]}} {{새로운_기가바이트_크기}}`
