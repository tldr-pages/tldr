# xcopy

> 파일과 폴더 트리를 복사합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- 파일(들)을 지정된 대상에 복사:

`xcopy {{경로\파일_또는_폴더}} {{경로\대상\폴더}}`

- 복사할 파일을 목록으로 표시:

`xcopy {{경로\파일_또는_폴더}} {{경로\대상\폴더}} /p`

- 폴더 구조만 복사하고 파일은 제외:

`xcopy {{경로\파일_또는_폴더}} {{경로\대상\폴더}} /t`

- 빈 폴더도 복사:

`xcopy {{경로\파일_또는_폴더}} {{경로\대상\폴더}} /e`

- 소스의 ACL을 대상에 유지:

`xcopy {{경로\파일_또는_폴더}} {{경로\대상\폴더}} /o`

- 네트워크 연결이 끊어졌을 때 재개 허용:

`xcopy {{경로\파일_또는_폴더}} {{경로\대상\폴더}} /z`

- 대상에 파일이 있을 때 대화형 프롬프트 비활성화:

`xcopy {{경로\파일_또는_폴더}} {{경로\대상\폴더}} /y`

- 도움말 표시:

`xcopy /?`
