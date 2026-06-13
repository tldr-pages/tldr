# wine

> Unix 기반 시스템에서 Windows 실행 파일을 실행.
> 더 많은 정보: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- `wine` 환경에서 특정 프로그램 실행:

`wine {{명령어}}`

- 백그라운드에서 특정 프로그램 실행:

`wine start {{명령어}}`

- MSI 패키지 설치/제거:

`wine msiexec /{{i|x}} {{경로/대상/패키지.msi}}`

- `파일 탐색기`, `메모장`, 또는 `워드패드` 실행:

`wine {{explorer|notepad|write}}`

- `레지스트리 편집기`, `제어판`, 또는 `작업 관리자` 실행:

`wine {{regedit|control|taskmgr}}`

- 설정 도구 실행:

`wine winecfg`
