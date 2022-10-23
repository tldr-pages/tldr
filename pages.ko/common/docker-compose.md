# docker compose

> 다중 컨테이너 도커 어플리케이션 실행 및 관리.
> 더 많은 정보: <https://docs.docker.com/compose/reference/>.

- 실행 중인 모든 컨테이너 목록 보기:

`docker compose ps`

- 현재 디렉토리의 `docker-compose.yml` 파일을 사용해 모든 컨테이너를 백그라운드에서 생성하고 실행하기:

`docker compose up -d`

- 모든 컨테이너 실행, 필요 시 재빌드:

`docker compose up --build`

- 특정 구성 파일을 사용해 모든 컨테이너 실행:

`docker compose --file {{경로/파일명}} up`

- 실행 중인 모든 컨테이너 중지:

`docker compose stop`

- 모든 컨테이너, 네트워크, 이미지, 볼륨 중지 및 삭제:

`docker compose down --rmi all --volumes`

- 모든 컨테이너에 대한 로그 팔로우:

`docker compose logs --follow`

- 특정 컨테이너에 대한 로그 팔로우:

`docker compose logs --follow {{컨테이너_이름}}`
