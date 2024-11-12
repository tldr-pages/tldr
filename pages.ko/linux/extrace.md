# extrace

> exec() 호출을 추적합니다.
> 더 많은 정보: <https://github.com/chneukirchen/extrace>.

- 시스템에서 발생하는 모든 프로그램 실행을 추적:

`sudo extrace`

- 명령을 실행하고 해당 명령의 하위 프로세스만 추적:

`sudo extrace {{명령}}`

- 각 프로세스의 현재 작업 디렉터리 출력:

`sudo extrace -d`

- 각 실행 파일의 전체 경로 해석:

`sudo extrace -l`

- 각 프로세스를 실행하는 사용자 표시:

`sudo extrace -u`
