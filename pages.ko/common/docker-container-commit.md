# docker commit

> 컨테이너의 변경 사항으로부터 새로운 이미지를 생성합니다.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/commit/>.

- 특정 컨테이너로부터 이미지 생성:

`docker commit {{컨테이너}} {{이미지}}:{{태그}}`

- 생성된 이미지에 `CMD` Dockerfile 명령 적용:

`docker commit {{[-c|--change]}} "CMD {{명령}}" {{컨테이너}} {{이미지}}:{{태그}}`

- 생성된 이미지에 `ENV` Dockerfile 명령 적용:

`docker commit {{[-c|--change]}} "ENV {{이름}}={{값}}" {{컨테이너}} {{이미지}}:{{태그}}`

- 메타데이터에 특정 작성자를 포함하여 이미지 생성:

`docker commit {{[-a|--author]}} "{{작성자}}" {{컨테이너}} {{이미지}}:{{태그}}`

- 메타데이터에 특정 주석을 포함하여 이미지 생성:

`docker commit {{[-m|--message]}} "{{주석}}" {{컨테이너}} {{이미지}}:{{태그}}`

- 커밋 중 컨테이너를 중지하지 않고 이미지 생성:

`docker commit {{[-p|--pause]}} {{false}} {{컨테이너}} {{이미지}}:{{태그}}`

- 도움말 표시:

`docker commit --help`
