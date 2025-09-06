# makensis

> NSIS 설치 프로그램을 위한 크로스 플랫폼 컴파일러.
> NSIS 스크립트를 Windows 설치 프로그램 실행 파일로 컴파일합니다.
> 더 많은 정보: <https://nsis.sourceforge.io/Docs/Chapter3.html>.

- NSIS 스크립트 컴파일:

`makensis {{경로/대상/파일.nsi}}`

- 엄격 모드로 NSIS 스크립트 컴파일 (경고를 오류로 처리):

`makensis -WX {{경로/대상/파일.nsi}}`

- 특정 명령에 대한 도움말 표시:

`makensis -CMDHELP {{명령}}`
