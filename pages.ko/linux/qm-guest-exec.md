# qm guest exec

> 게스트 에이전트를 통해 특정 명령 실행.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_guest_exec>.

- 게스트 에이전트를 통해 특정 명령 실행:

`qm guest exec {{가상_머신_ID}} {{명령어}} {{인수1 인수2 ...}}`

- 게스트 에이전트를 통해 비동기적으로 특정 명령 실행:

`qm guest exec {{가상_머신_ID}} {{인수1 인수2 ...}} --synchronous 0`

- 10초의 지정된 제한 시간으로 게스트 에이전트를 통해 특정 명령 실행:

`qm guest exec {{가상_머신_ID}} {{인수1 인수2 ...}} --timeout {{10}}`

- 게스트 에이전트를 통해 특정 명령 실행 및 `stdin`에서 EOF까지 입력을 게스트 에이전트로 전달:

`qm guest exec {{가상_머신_ID}} {{인수1 인수2 ...}} --pass-stdin 1`
