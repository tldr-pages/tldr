# <>

> 읽기와 쓰기가 모두 가능한 파일 디스크립터 열기.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Opening-File-Descriptors-for-Reading-and-Writing>.

- 파일을 읽기/쓰기 모드로 파일 디스크립터에 연결:

`exec {{3}}<>{{경로/대상/파일}}`

- 원격 TCP 연결을 파일 디스크립터로 열기:

`exec {{3}}<>/dev/{{tcp}}/{{원격_호스트}}/{{포트_번호}}`

- 파일 디스크립터 닫기:

`exec {{3}}<>-`
