# docker images

> 도커 이미지를 관리한다.
> 더 많은 정보: <https://docs.docker.com/engine/reference/commandline/images/>.

- 모든 도커 이미지 목록보기:

`docker images`

- 중간자를 포함한 모든 도커 이미지 목록보기:

`docker images -a`

- 잔잔한 모드로 결과 목록보기(수로 표현된 ID들만):

`docker images -q`

- 어떠한 컨테이너에서도 사용되지 않은 모든 도커 이미지 목록보기:

`docker images --filter dangling=true`
