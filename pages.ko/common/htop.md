# htop

> 실행 중인 프로세스에 대한 동적인 실시간 정보를 표시.
> `top`의 향상된 버전.
> 관련 항목: `top`, `atop`, `glances`, `btop`, `btm`.
> 더 많은 정보: <https://manned.org/htop>.

- `htop` 실행:

`htop`

- 특정 사용자가 소유한 프로세스만 표시하는 `htop`실행:

`htop {{[-u|--user]}} {{사용자명}}`

- 프로세스를 트리 구조로 표시해 부모-자식 관계를 확인:

`htop {{[-t|--tree]}}`

- 지정한 기준(`sort_item`)으로 프로세스 정렬 (사용 가능한 옵션은 `htop --sort help` 참고):

`htop {{[-s|--sort]}} {{sort_item}}`

- 업데이트 간격을 지정하여 `htop` 실행 (0.1초 단위, 예: 50 = 5초):

`htop {{[-d|--delay]}} {{50}}`

- 시스템 및 프로세스 변경 기능을 모두 비활성화:

`htop --readonly`

- `htop` 실행 중 대화형 명령어 확인:

`{{<F1>|<?>}}`

- 다른 탭으로 전환:

`<Tab>`
