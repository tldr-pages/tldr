# docker compose down

> `docker compose up`으로 생성된 컨테이너, 네트워크, 이미지, 볼륨을 중지하고 제거.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/compose/down/>.

- 모든 컨테이너와 네트워크 중지 및 제거:

`docker compose down`

- 컨테이너, 네트워크 및 서비스에서 사용된 모든 이미지 제거:

`docker compose down --rmi all`

- 컨테이너, 네트워크 및 커스텀 태그가 없는 이미지만 제거:

`docker compose down --rmi local`

- 컨테이너, 네트워크 및 모든 볼륨 제거:

`docker compose down {{[-v|--volumes]}}`

- 고아 컨테이너까지 포함하여 모든 항목 중지 및 제거:

`docker compose down --remove-orphans`

- 사용자 정의 Compose 파일을 사용하여 컨테이너 중지 및 제거:

`docker compose {{[-f|--file]}} {{경로/대상/구성파일}} down`

- 사용자 정의 타임아웃(초)을 설정하여 컨테이너 중지 및 제거:

`docker compose down {{[-t|--timeout]}} {{타임아웃}}`

- Compose 파일에 정의되지 않은 서비스의 컨테이너(고아 컨테이너) 제거:

`docker compose down --remove-orphans {{[-v|--volumes]}}`
