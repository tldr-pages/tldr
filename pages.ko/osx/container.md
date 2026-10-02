# container

> macOS에서 Linux 컨테이너를 경량 가상 머신으로 생성하고 실행.
> 더 많은 정보: <https://github.com/apple/container>.

- 컨테이너 서비스 시작 (컨테이너 실행 전에 필요):

`container system start`

- 이미지에서 컨테이너를 대화형으로 실행하고 종료 후 삭제:

`container run --rm {{[-it|--interactive --tty]}} {{이미지}} {{sh}}`

- 이름과 공개 포트를 지정하여 컨테이너를 백그라운드에서 실행:

`container run {{[-d|--detach]}} --name {{컨테이너_이름}} {{[-p|--publish]}} {{8080:80}} {{이미지}}`

- 실행 중인 컨테이너 내부에서 명령 실행:

`container exec {{[-it|--interactive --tty]}} {{컨테이너_이름}} {{sh}}`

- 모든 컨테이너 목록 표시 (실행 중이거나 중지된 컨테이너):

`container {{[ls|list]}} {{[-a|--all]}}`

- 컨테이너 로그를 실시간으로 출력:

`container logs {{[-f|--follow]}} {{컨테이너_이름}}`

- 디렉터리의 Dockerfile을 사용하여 이미지 빌드:

`container build {{[-t|--tag]}} {{이미지_이름}} {{경로/대상/디렉터리}}`

- 컨테이너 중지 또는 삭제:

`container {{stop|delete}} {{컨테이너_이름}}`
