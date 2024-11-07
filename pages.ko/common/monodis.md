# monodis

> Mono 공용 중간 언어(CIL) 디스어셈블러.
> 더 많은 정보: <https://www.mono-project.com/docs/tools+libraries/tools/monodis/>.

- 어셈블리를 텍스트 CIL로 디스어셈블:

`monodis {{경로/대상/어셈블리.exe}}`

- 출력 결과를 파일로 저장:

`monodis --output={{경로/대상/출력.il}} {{경로/대상/어셈블리.exe}}`

- 어셈블리에 대한 정보 표시:

`monodis --assembly {{경로/대상/어셈블리.dll}}`

- 어셈블리의 참조 목록:

`monodis --assemblyref {{경로/대상/어셈블리.exe}}`

- 어셈블리의 모든 메서드 나열:

`monodis --method {{경로/대상/어셈블리.exe}}`

- 어셈블리에 내장된 리소스 나열:

`monodis --manifest {{경로/대상/어셈블리.dll}}`

- 모든 내장 리소스를 현재 디렉터리로 추출:

`monodis --mresources {{경로/대상/어셈블리.dll}}`
