# rmdir

> 디렉토리와 그 내용을 삭제합니다.
> PowerShell에서 이 명령어는 `Remove-Item`의 별칭입니다. 이 문서는 명령 프롬프트(`cmd`) 버전의 `rmdir`를 기반으로 합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- 해당 PowerShell 명령어의 문서 보기:

`tldr remove-item`

- 빈 디렉토리 삭제:

`rmdir {{경로\대상\디렉토리}}`

- 디렉토리와 그 내용 재귀적으로 삭제:

`rmdir {{경로\대상\디렉토리}} /s`

- 디렉토리와 그 내용을 프롬프트 없이 재귀적으로 삭제:

`rmdir {{경로\대상\디렉토리}} /s /q`
