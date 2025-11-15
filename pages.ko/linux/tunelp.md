# tunelp

> 병렬 포트 장치의 다양한 매개변수를 설정하여 문제 해결 또는 성능 향상을 위한 도구.
> `util-linux`의 일부.
> 더 많은 정보: <https://manned.org/tunelp>.

- 병렬 포트 장치의 [s]상태 확인:

`tunelp --status {{/dev/lp0}}`

- 주어진 병렬 포트 [r]재설정:

`tunelp --reset {{/dev/lp0}}`

- 장치에 사용할 [i]RQ 지정, 각 IRQ는 인터럽트 라인을 나타냄:

`tunelp -i 5 {{/dev/lp0}}`

- 프린터에 문자를 출력하기 위해 주어진 횟수만큼 시도한 후, 지정된 시간만큼 [c]대기:

`tunelp --chars {{횟수}} --time {{시간_센티초}} {{/dev/lp0}}`

- 오류 발생 시 [a]중지 활성화 또는 비활성화 (기본적으로 비활성화됨):

`tunelp --abort {{on|off}}`
