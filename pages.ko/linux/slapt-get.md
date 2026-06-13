# slapt-get

> Slackware 패키지 관리를 위한 `apt`와 유사한 시스템.
> slapt-getrc 파일에서 패키지 소스를 구성해야 합니다.
> 더 많은 정보: <https://software.jaos.org/git/slapt-get/plain/README>.

- 사용 가능한 패키지 및 버전 목록 업데이트:

`slapt-get --update`

- 패키지를 설치하거나 최신 버전으로 업데이트:

`slapt-get --install {{패키지}}`

- 패키지 제거:

`slapt-get --remove {{패키지}}`

- 설치된 모든 패키지를 최신 버전으로 업그레이드:

`slapt-get --upgrade`

- 패키지 이름, 디스크 세트 또는 버전으로 패키지 검색:

`slapt-get --search {{쿼리}}`

- 패키지에 대한 정보 표시:

`slapt-get --show {{패키지}}`
