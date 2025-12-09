# docker logs

> 컨테이너 로그들을 출력한다.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- 컨테이너로부터 로그들을 출력하기:

`docker logs {{컨테이너_이름}}`

- 로그들을 출력하고 추적하기:

`docker logs {{[-f|--follow]}} {{컨테이너_이름}}`

- 최근 5줄만 출력하기:

`docker logs {{컨테이너_이름}} {{[-n|--tail]}} {{5}}`

- 로그들을 출력하고 타임스태프 추가하기:

`docker logs {{[-t|--timestamps]}} {{컨테이너_이름}}`

- 특정 시점의 컨테이너 실행 시점으로부터 로그 출력하기 (예시. 23m, 10s, 2013-01-02T13:23:37):

`docker logs {{컨테이너_이름}} --until {{시간}}`
