# eclean

> 저장소의 소스 파일과 바이너리 패키지를 정리.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Eclean>.

- 소스 파일 디렉터리 정리:

`sudo eclean distfiles`

- 바이너리 패키지 디렉터리 정리:

`sudo eclean packages`

- 설치되지 않은 패키지의 distfile만 정리하고, 설치된 패키지의 distfile은 유지:

`sudo eclean {{[-d|--deep]}} {{[-n|--package-names]}} distfiles`

- 설치되지 않은 패키지의 바이너리 패키지만 정리하고, 설치된 패키지의 바이너리는 유지:

`sudo eclean {{[-d|--deep]}} {{[-n|--package-names]}} packages`
