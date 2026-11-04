# podman import

> tarball을 가져와 파일 시스템 이미지로 저장.
> 관련 항목: `podman export`, `podman save`.
> 더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-import.1.html>.

- 로컬 tarball 파일을 가져와 이미지 생성:

`podman import {{경로/대상/tarball.tar}} {{이미지:태그}}`

- URL에서 tarball을 가져와 이미지 생성:

`podman import {{https://example.com/image.tar}} {{이미지:태그}}`

- 커밋 메시지를 추가하여 tarball 가져오기:

`podman import {{[-m|--message]}} "{{커밋_메시지}}" {{경로/대상/tarball.tar}} {{이미지:태그}}`

- 기본 명령을 설정하여 tarball 가져오기 (컨테이너 실행에 필요):

`podman import {{[-c|--change]}} CMD={{/bin/bash}} {{경로/대상/tarball.tar}} {{이미지:태그}}`
