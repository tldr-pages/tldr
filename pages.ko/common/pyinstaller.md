# pyinstaller

> Python 애플리케이션과 의존성을 하나의 패키지로 묶음.
> 더 많은 정보: <https://pyinstaller.org/en/stable/man/pyinstaller.html>.

- Python 스크립트를 폴더 형태의 번들로 패키징 (`dist/` 디렉터리에 생성):

`pyinstaller {{경로/대상/스크립트.py}}`

- Python 스크립트를 단일 실행 파일로 패키징:

`pyinstaller {{[-F|--onefile]}} {{경로/대상/스크립트.py}}`

- 콘솔 창 없이 GUI 애플리케이션 패키징:

`pyinstaller {{[-w|--windowed]}} {{경로/대상/스크립트.py}}`

- 생성될 실행 파일 이름 지정:

`pyinstaller {{[-n|--name]}} {{애플리케이션_이름}} {{경로/대상/스크립트.py}}`

- 실행 파일의 사용자 지정 아이콘 설정:

`pyinstaller {{[-i|--icon]}} {{경로/대상/아이콘.ico}} {{경로/대상/스크립트.py}}`

- 추가 데이터 파일 또는 디렉터리를 번들에 포함:

`pyinstaller --add-data "{{경로/대상/소스파일}}:{{목적지}}" {{경로/대상/스크립트.py}}`

- 도움말 표시:

`pyinstaller {{[-h|--help]}}`

- 버전 정보 표시:

`pyinstaller {{[-v|--version]}}`
