# docker network

> Docker 네트워크 생성 및 관리.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/network/>.

- Docker 데몬에서 사용 가능하고 구성된 모든 네트워크 나열:

`docker network ls`

- 사용자 정의 네트워크 생성:

`docker network create {{[-d|--driver]}} {{드라이버_이름}} {{네트워크_이름}}`

- 하나 이상의 네트워크에 대한 자세한 정보 표시:

`docker network inspect {{네트워크_이름1 네트워크_이름2 ...}}`

- 이름 또는 ID를 사용하여 네트워크에 컨테이너 연결:

`docker network connect {{네트워크_이름}} {{컨테이너_이름|ID}}`

- 네트워크에서 컨테이너 연결 해제:

`docker network disconnect {{네트워크_이름}} {{컨테이너_이름|ID}}`

- 사용되지 않는 모든 네트워크 제거 (어떤 컨테이너에도 참조되지 않음):

`docker network prune`

- 하나 이상의 사용되지 않는 네트워크 제거:

`docker network rm {{네트워크_이름1 네트워크_이름2 ...}}`
