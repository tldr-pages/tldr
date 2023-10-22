# add-apt-repository

> 적절한 저장소 정의를 관리합니다.
> 더 많은 정보: <https://manned.org/apt-add-repository>.

- 새로운 apt 레포지토리 추가:

`add-apt-repository {{레포지토리_스펙}}`

- apt 레포지토리 삭제:

`add-apt-repository --remove {{레포지토리_스펙}}`

- 저장소 추가 후 패키지 캐시 업데이트:

`add-apt-repository --update {{레포지토리_스펙}}`

- 저장소에서 소스 패키지를 다운로드하도록 허용:

`add-apt-repository --enable-source {{레포지토리_스펙}}`
