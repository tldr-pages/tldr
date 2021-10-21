# docker-compose

> 다중 도커 응용 프로그램 실행 및 관리합니다.
> 더 많은 정보: <https://docs.docker.com/compose/reference/>.

- 실행 중인 모든 컨테이너들 목록:

`docker-compose ps`

- 현재 디렉토리로로부터 `docker-compose.yml` 파일을 사용하여 백그라운드에서 모든 컨테이너들을 생성하고 실행하기:

`docker-compose up -d`

- 모든 컨테이너들을 실행하고, 필요 시 재조립:

`docker-compose up --build`

- 대체 구성 파일을 사용하여 모든 컨테이너들 실행하기:

`docker-compose --file {{경로/파일명}} up`

- 실행중인 모든 컨테이너들 중지하기:

`docker-compose stop`

- 모든 컨테이너들, 네트워크, 이미지, 그리고 볼륨을 중지하고 제거하기:

`docker-compose down --rmi all --volumes`

- 모든 컨테이너들에 대한 로그들 팔로우:

`docker-compose logs --follow`
