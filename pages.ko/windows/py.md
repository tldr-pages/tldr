# py

> 지정한 Python 버전으로 실행하는 Windows용 Python 실행기.
> 관련 항목: `python`.
> 더 많은 정보: <https://docs.python.org/using/windows.html#python-launcher-for-windows>.

- REPL(대화형 셸) 실행 (옵션으로 -c, -m 등 python에서 지원하는 인자 사용 가능):

`py {{python_인자}}`

- 특정 Python 파일 실행:

`py {{경로\대상\파일.py}}`

- 특정 Python 버전 실행 (버전이 없고 PYLAUNCHER_ALLOW_INSTALL 환경 변수가 설정된 경우에, Microsoft Store 또는 Winget을 통해 자동 설치):

`py {{-2|-3.7|...}}`

- 설치된 Python 버전 목록 표시:

`py --list`
