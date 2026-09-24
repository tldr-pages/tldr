# systemctl isolate

> 지정한 유닛과 그 의존성만 시작하고, 나머지 유닛은 모두 중지.
> `IgnoreOnIsolate=yes`가 설정된 유닛은 제외됨.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#isolate%20UNIT>.

- 특정 타겟으로 전환 (`.target` 확장자는 생략 가능):

`systemctl isolate {{target}}`

- 그래픽 모드 타겟으로 전환:

`systemctl isolate graphical.target`

- 복구 (싱글-유저) 모드로 전환:

`systemctl isolate rescue.target`

- 긴급 모드로 전환:

`systemctl isolate emergency.target`
