# sfdk

> Sailfish SDK의 프론트엔드 도구.
> `init`, `build-init`, `device`와 같은 하위 명령은 각각 별도의 사용 문서를 제공.
> 더 많은 정보: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/10-general/doc/module.adoc>.

- 특정 SailfishOS 버전 및 아키텍처 대상을 사용하도록, 현재 빌드 환경 설정:

`sfdk config target=SailfishOS-{{5.0.0.62}}-{{aarch64}}`

- 현재 디렉터리를 빌드 디렉터리로 초기화:

`sfdk build-init`

- 지정한 프로젝트의 RPM SPEC 파일에 정의된 빌드 단계 실행:

`sfdk -C {{경로/대상/프로젝트}} build`

- SailfishOS 5.0.0.62 armv7hl 빌드 대상의 저장소 목록 표시:

`sfdk -c 'target=SailfishOS-5.0.0.62-armv7hl' build-shell --maintain ssu lr`

- 패키지를 에뮬레이터에 배포:

`sfdk config device="{{Sailfish OS Emulator 5.0.0.62}}"; sfdk deploy --sdk`

- 도움말 표시:

`sfdk --help`

- 지정한 주제에 대한 도움말 표시:

`sfdk --help-{{building|testing|maintaining|ide|all}}`

- 버전 정보 표시:

`sfdk --version`
