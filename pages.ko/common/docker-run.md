# docker run

> 새로운 Docker 컨테이너에서 명령 실행.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/run/>.

- 태그가 지정된 이미지에서 새 컨테이너로 명령 실행:

`docker run {{이미지:태그}} {{명령}}`

- 백그라운드에서 새 컨테이너로 명령 실행하고 ID 표시:

`docker run --detach {{이미지}} {{명령}}`

- 일회성 컨테이너에서 대화형 모드와 가상 TTY로 명령 실행:

`docker run --rm --interactive --tty {{이미지}} {{명령}}`

- 전달된 환경 변수를 사용하여 새 컨테이너로 명령 실행:

`docker run --env '{{변수}}={{값}}' --env {{변수}} {{이미지}} {{명령}}`

- 바인드 마운트된 볼륨을 사용하여 새 컨테이너로 명령 실행:

`docker run --volume {{/경로/대상/호스트_경로}}:{{/경로/대상/컨테이너_경로}} {{이미지}} {{명령}}`

- 게시된 포트를 사용하여 새 컨테이너로 명령 실행:

`docker run --publish {{호스트_포트}}:{{컨테이너_포트}} {{이미지}} {{명령}}`

- 이미지의 엔트리포인트를 덮어쓰며 새 컨테이너로 명령 실행:

`docker run --entrypoint {{명령}} {{이미지}}`

- 네트워크에 연결하여 새 컨테이너로 명령 실행:

`docker run --network {{네트워크}} {{이미지}}`
