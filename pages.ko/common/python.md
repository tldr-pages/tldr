# python

> Python 언어 인터프리터.
> 더 많은 정보: <https://docs.python.org/using/cmdline.html>.

- REPL(대화형 셸) 시작:

`python`

- 특정 Python 파일 실행:

`python {{경로/대상/파일.py}}`

- 특정 Python 파일 실행 후 REPL 시작:

`python -i {{경로/대상/파일.py}}`

- Python 표현식 실행:

`python -c "{{표현식}}"`

- 지정된 라이브러리 모듈의 스크립트 실행:

`python -m {{모듈}} {{인자들}}`

- `pip`를 사용하여 패키지 설치:

`python -m pip install {{패키지}}`

- Python 스크립트 대화형 디버깅:

`python -m pdb {{경로/대상/파일.py}}`

- 현재 디렉터리에서 포트 8000으로 내장 HTTP 서버 시작:

`python -m http.server`
