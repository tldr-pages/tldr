# docker volume

> Docker 볼륨 관리.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/volume/>.

- 볼륨 생성:

`docker volume create {{볼륨_이름}}`

- 특정 레이블을 사용하여 볼륨 생성:

`docker volume create --label {{레이블}} {{볼륨_이름}}`

- 100 MiB의 크기와 1000의 uid를 가진 `tmpfs` 볼륨 생성:

`docker volume create --opt {{type}}={{tmpfs}} --opt {{device}}={{tmpfs}} --opt {{o}}={{size=100m,uid=1000}} {{볼륨_이름}}`

- 모든 볼륨 나열:

`docker volume ls`

- 볼륨 제거:

`docker volume rm {{볼륨_이름}}`

- 볼륨에 대한 정보 표시:

`docker volume inspect {{볼륨_이름}}`

- 사용되지 않는 모든 로컬 볼륨 제거:

`docker volume prune`

- 하위 명령에 대한 도움말 표시:

`docker volume {{서브커맨드}} --help`
