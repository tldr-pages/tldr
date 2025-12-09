# docker service

> Docker 데몬에서 서비스를 관리합니다.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/service/>.

- Docker 데몬에서 서비스 목록 나열:

`docker service ls`

- 새 서비스 생성:

`docker service create --name {{서비스_이름}} {{이미지}}:{{태그}}`

- 하나 이상의 서비스에 대한 자세한 정보 표시:

`docker service inspect {{서비스_이름_또는_ID1 서비스_이름_또는_ID2}}`

- 하나 이상의 서비스에 대한 작업 목록 나열:

`docker service ps {{서비스_이름_또는_ID1 서비스_이름_또는_ID2 ...}}`

- 공백으로 구분된 서비스 목록에 대해 특정 복제본 수로 확장:

`docker service scale {{서비스_이름}}={{복제본_수}}`

- 하나 이상의 서비스 제거:

`docker service rm {{서비스_이름_또는_ID1 서비스_이름_또는_ID2}}`
