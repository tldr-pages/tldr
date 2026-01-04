# qm guest

> VM 게스트 에이전트를 관리합니다.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_guest_cmd>.

- 특정 PID의 상태 출력:

`qm {{[g|guest]}} {{[exec-s|exec-status]}} {{가상_머신_ID}} {{pid}}`

- 가상 머신 내 특정 사용자에 대해 비밀번호를 대화식으로 설정:

`qm {{[g|guest]}} {{[p|passwd]}} {{가상_머신_ID}} {{사용자_명}}`

- 이미 해시된 비밀번호를 가상 머신 내 특정 사용자에 대해 대화식으로 설정:

`qm {{[g|guest]}} {{[p|passwd]}} {{가상_머신_ID}} {{사용자_명}} --crypted 1`

- 특정 QEMU 게스트 에이전트 명령 실행:

`qm {{[g|guest]}} {{[c|cmd]}} {{가상_머신_ID}} {{fsfreeze-freeze|fsfreeze-status|fsfreeze-thaw|fstrim|get-fsinfo|...}}`

- 게스트 에이전트를 통해 특정 명령 실행:

`qm {{[g|guest]}} exec {{가상_머신_ID}} {{명령어}} {{인수1 인수2 ...}}`

- 게스트 에이전트를 통해 비동기적으로 특정 명령 실행:

`qm {{[g|guest]}} exec {{가상_머신_ID}} {{인수1 인수2 ...}} --synchronous 0`

- 10초의 지정된 제한 시간으로 게스트 에이전트를 통해 특정 명령 실행:

`qm {{[g|guest]}} exec {{가상_머신_ID}} {{인수1 인수2 ...}} --timeout {{10}}`

- 게스트 에이전트를 통해 특정 명령 실행 및 `stdin`에서 EOF까지 입력을 게스트 에이전트로 전달:

`qm {{[g|guest]}} exec {{가상_머신_ID}} {{인수1 인수2 ...}} --pass-stdin 1`
