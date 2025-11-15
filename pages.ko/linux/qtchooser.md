# qtchooser

> Qt 개발 바이너리 버전 간 선택을 돕는 래퍼.
> 더 많은 정보: <https://manned.org/qtchooser>.

- 구성 파일에서 사용 가능한 Qt 버전 나열:

`qtchooser --list-versions`

- 환경 정보 출력:

`qtchooser --print-env`

- 지정된 Qt 버전을 사용하여 지정된 도구 실행:

`qtchooser --run-tool={{도구}} --qt={{버전_이름}}`

- 선택할 수 있도록 Qt 버전 항목 추가:

`qtchooser --install {{버전_이름}} {{경로/대상/qmake}}`

- 도움말 표시:

`qtchooser --help`
