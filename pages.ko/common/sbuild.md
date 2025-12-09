# sbuild

> 깨끗한 `chroot` 환경에서 Debian 바이너리 패키지를 빌드.
> 더 많은 정보: <https://wiki.debian.org/sbuild>.

- 현재 디렉터리에서 패키지 빌드:

`sbuild`

- 지정된 패키지 빌드:

`sbuild {{패키지}}`

- 특정 배포판을 위해 빌드:

`sbuild --dist {{배포판}}`

- 사용자 지정 의존성을 사용하여 빌드 (디렉터리를 전달하면, `.deb`로 끝나는 모든 파일이 사용됨):

`sbuild --extra-package {{경로/대상/파일_또는_폴더}}`

- 빌드 실패 시 문제를 더 조사하기 위해 셸 실행:

`sbuild --build-failed-commands=%SBUILD_SHELL`

- 특정 아키텍처에 대해 크로스 빌드:

`sbuild --host {{아키텍처}}`

- 지정된 네이티브 아키텍처에 대해 빌드:

`sbuild --arch {{아키텍처}}`
