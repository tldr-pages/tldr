# icoextract

> Windows 실행 파일(`.exe`, `.dll`, `.mun`)에서 아이콘을 추출하여 ICO 파일로 저장.
> 관련 항목: `icolist`.
> 더 많은 정보: <https://github.com/jlu5/icoextract>.

- 실행 파일에서 아이콘을 추출하여 ICO 파일로 저장:

`icoextract {{경로/대상/입력_파일.exe}} {{경로/대상/출력_파일.ico}}`

- 인덱스별로 특정 아이콘 추출:

`icoextract {{[-n|--num]}} {{인덱스}} {{경로/대상/입력_파일.exe}} {{경로/대상/출력_파일.ico}}`

- 리소스 ID별로 아이콘 추출:

`icoextract {{[-i|--id]}} {{리소스_id}} {{경로/대상/입력_파일.exe}} {{경로/대상/출력_파일.ico}}`

- 상세/디버그 로깅을 활성화하여 실행:

`icoextract {{[-v|--verbose]}} {{경로/대상/입력_파일.exe}} {{경로/대상/출력_파일.ico}}`

- 도움말 표시:

`icoextract {{[-h|--help]}}`

- 버전 표시:

`icoextract {{[-V|--version]}}`
