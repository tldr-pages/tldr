# wipefs

> 파일 시스템, RAID, 또는 파티션 테이블 서명을 장치에서 삭제합니다.
> 더 많은 정보: <https://manned.org/wipefs>.

- 지정된 장치의 서명 표시:

`sudo wipefs {{/dev/sdX}}`

- 특정 장치의 모든 사용 가능한 서명 유형을 파티션을 재귀적으로 탐색하지 않고 삭제:

`sudo wipefs --all {{/dev/sdX}}`

- 글롭 패턴을 사용하여 장치 및 파티션의 모든 사용 가능한 서명 유형 삭제:

`sudo wipefs --all {{/dev/sdX}}*`

- 시뮬레이션 실행:

`sudo wipefs --all --no-act {{/dev/sdX}}`

- 파일 시스템이 마운트되어 있어도 강제로 삭제:

`sudo wipefs --all --force {{/dev/sdX}}`
