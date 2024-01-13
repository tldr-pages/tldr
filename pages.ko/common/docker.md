# docker

> 도커 컨테이너들과 이미지들을 관리한다.
> 더 많은 정보: <https://docs.docker.com/engine/reference/commandline/cli/>.

- 모든 도커 컨테이너들(실행중이고 중지된) 목록 보기:

`docker ps --all`

- 사용자 정의 이름으로 이미지로부터 컨테이너 실행:

`docker run --name {{컨테이너_이름}} {{이미지}}`

- 기존 컨테이너 실행 또는 중지하기:

`docker {{실행|중지}} {{컨테이너_이름}}`

- 도커 레지스트리로부터 이미지 가져오기:

`docker pull {{이미지}}`

- 이미 실행중인 컨테이너 내부에서 쉘 열기:

`docker exec -it {{컨테이너_이름}} {{쉘}}`

- 중지된 컨테이너 제거하기:

`docker rm {{컨테이너_이름}}`

- 컨테이너 로그를 가져오고 팔로우하기:

`docker logs -f {{컨테이너_이름}}`
