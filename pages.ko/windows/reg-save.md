# reg save

> 레지스트리 키, 하위 키 및 값을 네이티브 `.hiv` 파일로 저장합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-save>.

- 레지스트리 키, 하위 키 및 값을 특정 파일로 저장:

`reg save {{키_이름}} {{경로\대상\파일.hiv}}`

- 기존 파일을 강제로 (예라고 가정) 덮어쓰기:

`reg save {{키_이름}} {{경로\대상\파일.hiv}} /y`
