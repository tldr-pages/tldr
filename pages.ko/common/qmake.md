# qmake

> Qt 프로젝트 파일로부터 Makefile을 생성.
> 더 많은 정보: <https://doc.qt.io/qt-6/qmake-running.html>.

- 현재 디렉터리의 프로젝트 파일에서 `Makefile` 생성:

`qmake`

- `Makefile`과 프로젝트 파일의 위치 지정:

`qmake -o {{경로/대상/Makefile}} {{경로/대상/project_file.pro}}`

- 기본 프로젝트 파일 생성:

`qmake -project`

- 프로젝트 컴파일:

`qmake && make`

- 디버그 모드 활성화:

`qmake -d`

- 도움말 표시:

`qmake -help`
