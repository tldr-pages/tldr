# reg

> Windows 레지스트리에서 키와 값을 관리.
> `add`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg>.

- 레지스트리 명령 실행:

`reg {{명령}}`

- 하위 키 추가 및 복사에 대한 문서 보기:

`tldr reg {{add|copy}}`

- 키 및 하위 키 삭제에 대한 문서 보기:

`tldr reg {{delete|unload}}`

- 키 검색, 보기 및 비교에 대한 문서 보기:

`tldr reg {{compare|flags|query}}`

- 레지스트리 키를 내보내고 가져오면서 키 소유권 및 ACL을 보존하지 않는 것에 대한 문서 보기:

`tldr reg {{export|import}}`

- 키 소유권 및 ACL을 보존하면서 레지스트리를 저장, 복원 및 언로드하는 것에 대한 문서 보기:

`tldr reg {{save|restore|load|unload}}`

- 도움말 표시:

`reg /?`

- 특정 명령에 대한 도움말 표시:

`reg {{명령}} /?`
