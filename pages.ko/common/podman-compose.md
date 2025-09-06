# podman-compose

> Compose Specification 컨테이너 정의를 실행하고 관리.
> 더 많은 정보: <https://github.com/containers/podman-compose>.

- 실행 중인 모든 컨테이너 나열:

`podman-compose ps`

- 로컬 `docker-compose.yml`을 사용하여 백그라운드에서 모든 컨테이너 생성 및 시작:

`podman-compose up -d`

- 필요한 경우 빌드하여 모든 컨테이너 시작:

`podman-compose up --build`

- 다른 컴포즈 파일을 사용하여 모든 컨테이너 시작:

`podman-compose {{[-f|--file]}} {{경로/대상/파일.yaml}} up`

- 실행 중인 모든 컨테이너 중지:

`podman-compose stop`

- 모든 컨테이너, 네트워크 및 볼륨 제거:

`podman-compose down --volumes`

- 컨테이너의 로그를 실시간으로 팔로우 (모든 컨테이너 이름 생략):

`podman-compose logs --follow {{컨테이너_이름}}`

- 포트 매핑 없이 서비스에서 일회성 명령 실행:

`podman-compose run {{서비스_이름}} {{명령}}`
