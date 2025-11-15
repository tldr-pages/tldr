# reg export

> 지정된 하위 키와 값을 `.reg` 파일로 내보냅니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-export>.

- 특정 키의 모든 하위 키와 값을 내보내기:

`reg export {{키_이름}} {{경로\대상\파일.reg}}`

- 기존 파일을 강제로 ([y]es로 가정) 덮어쓰기:

`reg export {{키_이름}} {{경로\대상\파일.reg}} /y`
