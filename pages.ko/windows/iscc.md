# iscc

> Inno Setup 설치 프로그램용 컴파일러입니다.
> 이는 Inno Setup 스크립트를 Windows 설치 프로그램 실행 파일로 컴파일합니다.
> 더 많은 정보: <https://jrsoftware.org/isinfo.php>.

- Inno Setup 스크립트를 컴파일:

`iscc {{경로\대상\파일.iss}}`

- Inno Setup 설치 프로그램을 조용히 컴파일:

`iscc /Q {{경로\대상\파일.iss}}`

- 서명된 Inno Setup 설치 프로그램 컴파일:

`iscc /S={{이름}}={{명령어}} {{경로\대상\파일.iss}}`
