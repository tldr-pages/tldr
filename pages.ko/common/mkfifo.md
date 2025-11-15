# mkfifo

> FIFO(이름 있는 파이프) 생성.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>.

- 지정된 경로에 이름 있는 파이프 생성:

`mkfifo {{경로/대상/파이프}}`

- 이름 있는 파이프를 통해 데이터를 보내고 명령을 백그라운드로 전송:

`echo "{{Hello World}}" > {{경로/대상/파이프}} &`

- 이름 있는 파이프를 통해 데이터 수신:

`cat {{경로/대상/파이프}}`

- 터미널 세션을 실시간으로 공유:

`mkfifo {{경로/대상/파이프}}; script -f {{경로/대상/파이프}}`
