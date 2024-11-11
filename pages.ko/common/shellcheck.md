# shellcheck

> 쉘 스크립트를 정적으로 검사하여 오류, 사용 중단된/안전하지 않은 기능 및 잘못된 관행을 확인합니다.
> 더 많은 정보: <https://github.com/koalaman/shellcheck/wiki>.

- 쉘 스크립트 검사:

`shellcheck {{경로/대상/스크립트.sh}}`

- 스크립트 상단의 셰뱅을 무시하고 지정된 [s]쉘 방언으로 쉘 스크립트를 검사:

`shellcheck --shell {{sh|bash|dash|ksh}} {{경로/대상/스크립트.sh}}`

- 하나 이상의 오류 유형을 무시:

`shellcheck --exclude {{SC1009,SC1073,...}} {{경로/대상/스크립트.sh}}`

- 소스된 쉘 스크립트도 검사:

`shellcheck --check-sourced {{경로/대상/스크립트.sh}}`

- 지정된 [f]포맷으로 출력 표시 (기본값은 `tty`):

`shellcheck --format {{tty|checkstyle|diff|gcc|json|json1|quiet}} {{경로/대상/스크립트.sh}}`

- 하나 이상의 [o]선택적 검사 활성화:

`shellcheck --enable {{add-default-case,avoid-nullary-conditions,...}} {{경로/대상/스크립트.sh}}`

- 기본적으로 비활성화된 모든 사용 가능한 선택적 검사 목록 나열:

`shellcheck --list-optional`

- 고려할 [S]심각도 수준 조정 (기본값은 `style`):

`shellcheck --severity {{error|warning|info|style}} {{경로/대상/스크립트.sh}}`
