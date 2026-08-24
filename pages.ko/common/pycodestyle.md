# pycodestyle

> Python 코드를 PEP 8 스타일 규칙에 맞게 검사.
> 더 많은 정보: <https://pycodestyle.pycqa.org/en/latest/intro.html#example-usage-and-output>.

- 단일 파일의 스타일 검사:

`pycodestyle {{파일.py}}`

- 여러 파일의 스타일 검사:

`pycodestyle {{파일1.py 파일2.py ...}}`

- 오류의 첫 번째 발생만 표시:

`pycodestyle --first {{파일.py}}`

- 각 오류에 대한 소스 코드 표시:

`pycodestyle --show-source {{파일.py}}`

- 각 오류에 대한 특정 PEP 8 텍스트 표시:

`pycodestyle --show-pep8 {{파일.py}}`
