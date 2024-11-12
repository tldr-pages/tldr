# systemd-tty-ask-password-agent

> 보류 중인 systemd 비밀번호 요청 목록을 표시하거나 처리합니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-tty-ask-password-agent.html>.

- 현재 보류 중인 모든 시스템 비밀번호 요청 목록 표시:

`systemd-tty-ask-password-agent --list`

- 비밀번호 요청을 지속적으로 처리:

`systemd-tty-ask-password-agent --watch`

- 호출하는 TTY에서 사용자에게 질문하여 현재 보류 중인 시스템 비밀번호 요청 처리:

`systemd-tty-ask-password-agent --query`

- 호출하는 TTY에서 사용자에게 질문하는 대신 wall로 비밀번호 요청 전달:

`systemd-tty-ask-password-agent --wall`
