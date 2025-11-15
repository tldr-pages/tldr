# takeout

> Docker 기반의 개발 전용 의존성 관리자.
> 더 많은 정보: <https://github.com/tighten/takeout>.

- 사용 가능한 서비스 목록 표시:

`takeout enable`

- 특정 서비스 활성화:

`takeout enable {{이름}}`

- 기본 매개변수로 특정 서비스 활성화:

`takeout enable --default {{이름}}`

- 활성화된 서비스 목록 표시:

`takeout disable`

- 특정 서비스 비활성화:

`takeout disable {{이름}}`

- 모든 서비스 비활성화:

`takeout disable --all`

- 특정 컨테이너 시작:

`takeout start {{컨테이너_ID}}`

- 특정 컨테이너 중지:

`takeout stop {{컨테이너_ID}}`
