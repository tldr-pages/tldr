# apt-get

> Debian 및 Ubuntu 패키지 관리 도구.
> `apt-cache`를 사용하여 패키지를 검색하세요.
> Ubuntu 16.04 이후 버전에서는 대화형 사용 시 `apt` 사용을 권장합니다.
> 더 많은 정보: <https://manned.org/apt-get.8>.

- 사용 가능한 패키지 및 버전 목록 업데이트 (다른 `apt-get` 명령어 실행 전에 권장됨):

`sudo apt-get update`

- 패키지 설치 또는 최신 버전으로 업데이트:

`sudo apt-get install {{패키지}}`

- 패키지 제거:

`sudo apt-get remove {{패키지}}`

- 패키지 및 구성 파일 제거:

`sudo apt-get purge {{패키지}}`

- 설치된 모든 패키지를 최신 버전으로 업그레이드:

`sudo apt-get upgrade`

- 로컬 저장소 정리 - 중단된 다운로드로 인해 더 이상 다운로드할 수 없는 패키지 파일(`.deb`) 제거:

`sudo apt-get autoclean`

- 더 이상 필요하지 않은 모든 패키지 제거:

`sudo apt-get autoremove`

- 설치된 패키지 업그레이드 (`upgrade`와 유사하지만, 불필요한 패키지를 제거하고 새로운 의존성을 충족하기 위해 추가 패키지를 설치):

`sudo apt-get dist-upgrade`
