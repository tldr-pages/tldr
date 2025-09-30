# web-ext

> 웹 확장 프로그램 개발을 관리하는 명령줄 도구.
> 더 많은 정보: <https://github.com/mozilla/web-ext>.

- 현재 디렉터리에 있는 웹 확장 프로그램을 Firefox에서 실행:

`web-ext run`

- 특정 디렉터리에서 웹 확장 프로그램을 Firefox에서 실행:

`web-ext run --source-dir {{경로/대상/폴더}}`

- 자세한 실행 출력 표시:

`web-ext run --verbose`

- Firefox Android에서 웹 확장 프로그램 실행:

`web-ext run --target firefox-android`

- 매니페스트 및 소스 파일의 오류 검사:

`web-ext lint`

- 확장 프로그램 빌드 및 패키징:

`web-ext build`

- 자세한 빌드 출력 표시:

`web-ext build --verbose`

- 자체 호스팅을 위한 패키지 서명:

`web-ext sign --api-key {{api_키}} --api-secret {{api_비밀}}`
