# apt list

> 패키지 목록 표시.
> 참고: 로컬 패키지 인덱스를 최신 상태로 갱신하기 위해, 먼저 `apt update` 실행 권장.
> 더 많은 정보: <https://manned.org/apt.8>.

- 사용 가능한 모든 패키지 목록 표시:

`apt list`

- 패키지 이름만으로 목록 표시 (* 같은 와일드카드 지원):

`apt list {{패키지}}`

- 설치된 패키지 목록 표시:

`apt list {{[-i|--installed]}}`

- 업그레이드 가능한 패키지 목록 표시:

`apt list {{[-u|--upgradable]}}`
