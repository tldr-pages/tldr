# pro

> Ubuntu Pro 서비스 관리.
> 더 많은 정보: <https://manned.org/ubuntu-advantage.1>.

- 시스템을 Ubuntu Pro 지원 계약에 연결:

`sudo pro attach`

- Ubuntu Pro 서비스 상태 표시:

`pro status`

- 특정 취약점에 시스템이 영향을 받는지 확인 (가능하다면 수정 적용):

`pro fix {{CVE-번호}}`

- 지원되지 않는 패키지 수 표시:

`pro security-status`

- 더 이상 다운로드할 수 없는 패키지 나열:

`pro security-status --unavailable`

- 서드파티 패키지 나열:

`pro security-status --thirdparty`
