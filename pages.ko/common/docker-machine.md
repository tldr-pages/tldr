# docker-machine

> 도커를 실행하는 머신들을 생성하고 관리한다.
> 더 많은 정보: <https://github.com/docker/machine>.

- 현재 실행중인 도커 머신들 목록보기:

`docker-machine ls`

- 특정 이름으로 새로운 도커 머신 생성하기:

`docker-machine create {{이름}}`

- 머신의 상태 가져오기:

`docker-machine status {{이름}}`

- 머신 시작하기:

`docker-machine start {{이름}}`

- 머신 중지하기:

`docker-machine stop {{이름}}`

- 머신에 대한 정보 검사하기:

`docker-machine inspect {{이름}}`
