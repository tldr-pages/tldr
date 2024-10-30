# docker update

> Docker 컨테이너의 구성 업데이트.
> 이 명령은 Windows 컨테이너에서는 지원되지 않습니다.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/update/>.

- 특정 컨테이너가 종료될 때 적용할 재시작 정책 업데이트:

`docker update --restart={{always|no|on-failure|unless-stopped}} {{컨테이너_이름}}`

- 특정 컨테이너가 0이 아닌 종료 상태로 종료될 때 최대 3번까지 재시작하는 정책 업데이트:

`docker update --restart=on-failure:3 {{컨테이너_이름}}`

- 특정 컨테이너에 사용할 수 있는 CPU 수 업데이트:

`docker update --cpus {{개수}} {{컨테이너_이름}}`

- 특정 컨테이너의 메모리 제한을 [M]egabytes 단위로 업데이트:

`docker update --memory {{제한값}}M {{컨테이너_이름}}`

- 특정 컨테이너 내에서 허용되는 최대 프로세스 ID 수 업데이트 (`-1`은 무제한):

`docker update --pids-limit {{개수}} {{컨테이너_이름}}`

- 특정 컨테이너가 디스크로 스왑할 수 있는 메모리 양을 [M]egabytes 단위로 업데이트 (`-1`은 무제한):

`docker update --memory-swap {{제한값}}M {{컨테이너_이름}}`
