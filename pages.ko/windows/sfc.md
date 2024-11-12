# sfc

> Windows 시스템 파일의 무결성을 검사합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/sfc>.

- 명령어 사용 정보 표시:

`sfc`

- 모든 시스템 파일을 검사하고 가능하면 문제 수정:

`sfc /scannow`

- 모든 시스템 파일을 검사하고 문제 수정 시도 없음:

`sfc /verifyonly`

- 특정 파일을 검사하고 가능하면 문제 수정:

`sfc /scanfile={{경로\대상\파일}}`

- 특정 파일을 검사하고 문제 수정 시도 없음:

`sfc /verifyfile={{경로\대상\파일}}`

- 오프라인 복구 시 부팅 디렉터리 지정:

`sfc /offbootdir={{경로\대상\폴더}}`

- 오프라인 복구 시 Windows 디렉터리 지정:

`sfc /offwindir={{경로\대상\폴더}}`
