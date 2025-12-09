# systemd-ask-password

> 시스템 비밀번호를 사용자에게 요청.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-ask-password.html>.

- 특정 메시지와 함께 시스템 비밀번호 요청:

`systemd-ask-password "{{메시지}}"`

- 비밀번호 요청에 식별자 지정:

`systemd-ask-password --id={{식별자}} "{{메시지}}"`

- 커널 키링 키 이름을 비밀번호 캐시로 사용:

`systemd-ask-password --keyname={{키_이름}} "{{메시지}}"`

- 비밀번호 요청에 사용자 정의 시간 초과 설정:

`systemd-ask-password --timeout={{초}} "{{메시지}}"`

- 에이전트 시스템을 강제로 사용하고 현재 TTY에서 묻지 않음:

`systemd-ask-password --no-tty "{{메시지}}"`

- 비밀번호를 표시하지 않고 커널 키링에 저장:

`systemd-ask-password --no-output --keyname={{키_이름}} "{{메시지}}"`
