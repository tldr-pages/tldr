# deb-get

> 타사 저장소 또는 직접 다운로드를 통해 배포된 `.deb` 패키지에 대한 `apt-get` 기능.
> `apt-get`을 사용하는 Linux 배포판과 함께 작동합니다.
> 더 많은 정보: <https://github.com/wimpysworld/deb-get>.

- 사용 가능한 패키지 및 버전 목록 업데이트:

`deb-get update`

- 특정 패키지 검색:

`deb-get search {{패키지}}`

- 패키지 정보 표시:

`deb-get show {{패키지}}`

- 패키지 설치 또는 최신 버전으로 업데이트:

`deb-get install {{패키지}}`

- 패키지 제거 (`purge`를 사용하면 구성 파일도 제거):

`deb-get remove {{패키지}}`

- 설치된 모든 패키지를 최신 버전으로 업그레이드:

`deb-get upgrade`

- 사용 가능한 모든 패키지 나열:

`deb-get list`
