# docker images

> 도커 이미지 관리.
> 더 많은 정보: <https://docs.docker.com/engine/reference/commandline/images/>.

- 모든 도커 이미지 목록 보기:

`docker images`

- 중간 레이어를 포함한 도커 이미지 목록 보기:

`docker images --all`

- 조용한 모드로 결과 목록 보기 (이미지 ID만 출력):

`docker images --quiet`

- 어떤 컨테이너에도 사용되지 않은 도커 이미지 목록 보기:

`docker images --filter dangling=true`

- 이름에 부분 문자열을 포함한 이미지 목록 보기:

`docker images "{{*이름*}}"`
