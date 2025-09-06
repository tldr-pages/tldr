# docker

> Docker 컨테이너 및 이미지를 관리.
> `run`과 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/>.

- 모든 도커 컨테이너들(실행 및 중지) 목록 보기:

`docker ps {{[-a|--all]}}`

- 사용자 정의 이름으로 이미지로부터 컨테이너 실행:

`docker run --name {{컨테이너_이름}} {{이미지}}`

- 기존 컨테이너 시작 또는 중지:

`docker {{start|stop}} {{컨테이너_이름}}`

- 도커 레지스트리로부터 이미지 가져오기:

`docker pull {{이미지}}`

- 이미 다운로드한 이미지 목록 표시:

`docker images`

- 실행 중인 컨테이너 내부에서 Bourne 셸(`sh`)과 함께 [i]nteractive [t]ty 열기:

`docker exec {{[-it|--interactive --tty]}} {{컨테이너_이름}} {{sh}}`

- 중지된 컨테이너 제거:

`docker rm {{컨테이너_이름}}`

- 컨테이너의 로그 가져오기 및 실시간으로 보기:

`docker logs {{[-f|--follow]}} {{컨테이너_이름}}`
