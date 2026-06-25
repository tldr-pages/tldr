# openclaw message

> OpenClaw 채널을 통해 메시지를 전송.
> 더 많은 정보: <https://docs.openclaw.ai/cli/message>.

- 전화번호로 메시지 전송 (WhatsApp):

`openclaw message send {{[-t|--target]}} {{+1234567890}} {{[-m|--message]}} "{{Hello}}"`

- 특정 채널로 메시지 전송:

`openclaw message send --channel {{telegram}} {{[-t|--target]}} {{사용자_아이디}} {{[-m|--message]}} "{{Hello}}"`

- 도움말 표시:

`openclaw message {{[-h|--help]}}`
