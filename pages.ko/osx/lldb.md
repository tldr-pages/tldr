# lldb

> LLVM 저수준 디버거.
> 더 많은 정보: <https://lldb.llvm.org/man/lldb.html>.

- 실행 파일 디버그:

`lldb "{{실행_파일}}"`

- 주어진 PID로 실행 중인 프로세스에 `lldb` 연결:

`lldb -p {{프로세스_ID}}`

- 주어진 이름의 새로운 프로세스가 시작될 때까지 기다렸다가 연결:

`lldb -w -n "{{프로세스_이름}}"`
