# reg query

> 레지스트리의 키와 하위 키의 값을 표시.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-query>.

- 키의 모든 값 표시:

`reg query {{키_이름}}`

- 키의 특정 [값] 표시:

`reg query {{키_이름}} /v {{값}}`

- 키와 하위 키의 모든 값 표시:

`reg query {{키_이름}} /s`

- 특정 패턴과 일치하는 키와 값을 [검색]:

`reg query {{키_이름}} /f "{{검색_패턴}}"`

- 지정된 데이터 [형식]과 일치하는 키의 값 표시:

`reg query {{키_이름}} /t REG_{{SZ|MULTI_SZ|EXPAND_SZ|DWORD|BINARY|NONE}}`

- 데이터에서만 검색:

`reg query {{키_이름}} /d`

- 키 이름에서만 검색:

`reg query {{키_이름}} /f "{{검색_패턴}}" /k`

- [대소문자] 구분하여 [정확히] 일치하는 값 검색:

`reg query {{키_이름}} /c /e`
