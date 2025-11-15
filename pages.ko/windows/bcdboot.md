# bcdboot

> 부트 파일을 구성하거나 복구.
> 더 많은 정보: <https://learn.microsoft.com/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di>.

- 소스 Windows 폴더의 BCD 파일을 사용하여 시스템 파티션 초기화:

`bcdboot {{C:\Windows}}`

- [v]erbose 모드 활성화:

`bcdboot {{C:\Windows}} /v`

- 시스템 파티션의 볼륨 문자 지정:

`bcdboot {{C:\Windows}} /s {{S:}}`

- [l]ocale 지정:

`bcdboot {{C:\Windows}} /l {{en-us}}`

- 지정된 볼륨으로 부트 파일을 복사할 때 [f]irmware 유형 지정:

`bcdboot {{C:\Windows}} /s {{S:}} /f {{UEFI|BIOS|ALL}}`
