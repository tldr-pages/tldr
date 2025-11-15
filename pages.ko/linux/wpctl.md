# wpctl

> WirePlumber를 관리하는 도구로, PipeWire의 세션 및 정책 관리자를 관리합니다.
> 참고: `id` 대신 특별한 이름인 `@DEFAULT_SINK@`을 사용하여 기본 싱크를 조작할 수 있습니다.
> 더 많은 정보: <https://pipewire.pages.freedesktop.org/wireplumber/>.

- WirePlumber가 관리하는 모든 객체 나열:

`wpctl status`

- 객체의 모든 속성 출력:

`wpctl inspect {{id}}`

- 객체를 해당 그룹의 기본값으로 설정:

`wpctl set-default {{id}}`

- 싱크의 볼륨 가져오기:

`wpctl get-volume {{id}}`

- 싱크의 볼륨을 `n` 퍼센트로 설정:

`wpctl set-volume {{id}} {{n}}%`

- 싱크의 볼륨을 `n` 퍼센트만큼 증가/감소:

`wpctl set-volume {{id}} {{n}}%{{+|-}}`

- 싱크 음소거/음소거 해제 설정 (1은 음소거, 0은 음소거 해제):

`wpctl set-mute {{id}} {{1|0|toggle}}`
