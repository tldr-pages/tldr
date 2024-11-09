# reg add

> 레지스트리에 새 키와 값을 추가.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add>.

- 새 레지스트리 키 추가:

`reg add {{키_이름}}`

- 특정 키 아래에 새 [v]alue 추가:

`reg add {{키_이름}} /v {{값}}`

- 특정 [d]ata로 새 값 추가:

`reg add {{키_이름}} /d {{데이터}}`

- 특정 데이터 [t]ype으로 키에 새 값 추가:

`reg add {{키_이름}} /t REG_{{SZ|MULTI_SZ|DWORD_BIG_ENDIAN|DWORD|BINARY|DWORD_LITTLE_ENDIAN|LINK|FULL_RESOURCE_DESCRIPTOR|EXPAND_SZ}}`

- [f]orcefully (프롬프트 없이) 기존 레지스트리 값 덮어쓰기:

`reg add {{키_이름}} /f`
