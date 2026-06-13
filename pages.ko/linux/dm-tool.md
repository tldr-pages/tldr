# dm-tool

> 디스플레이 관리자와 통신하는 도구.
> 더 많은 정보: <https://manned.org/dm-tool>.

- 현재 데스크톱 세션을 열어두고 로그인한 사용자가 인증하면 복원되도록 하면서 그리터 표시:

`dm-tool switch-to-greeter`

- 현재 세션 잠금:

`dm-tool lock`

- 특정 사용자로 전환하며 필요 시 인증 프롬프트 표시:

`dm-tool switch-to-user {{사용자명}} {{세션}}`

- 실행 중인 LightDM 세션 내에서 동적 시트 추가:

`dm-tool add-seat {{xlocal}} {{이름}}={{값}}`
