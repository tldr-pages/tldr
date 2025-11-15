# docker stats

> 컨테이너의 리소스 사용 통계를 실시간 스트림으로 표시.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/stats/>.

- 실행 중인 모든 컨테이너의 통계를 실시간 스트림으로 표시:

`docker stats`

- 하나 이상의 컨테이너에 대한 통계를 실시간 스트림으로 표시:

`docker stats {{컨테이너1 컨테이너2 ...}}`

- 컨테이너의 CPU 사용률을 표시하도록 열 형식을 변경:

`docker stats --format "{{.Name}}:\t{{.CPUPerc}}"`

- 모든 컨테이너(실행 중 및 중지된)의 통계를 표시:

`docker stats {{[-a|--all]}}`

- 스트리밍 통계를 비활성화하고 현재 통계만 가져오기:

`docker stats --no-stream`
