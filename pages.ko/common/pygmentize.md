# pygmentize

> Python 기반의 문법 하이라이터.
> 더 많은 정보: <https://pygments.org/docs/cmdline/>.

- 파일의 문법을 하이라이트하여 `stdout`에 출력 (파일 확장자로 언어 추론):

`pygmentize {{파일.py}}`

- 문법 하이라이트를 위한 언어를 명시적으로 설정:

`pygmentize -l {{자바스크립트}} {{입력_파일}}`

- 사용 가능한 렉서(입력 언어 처리기) 목록 표시:

`pygmentize -L lexers`

- 출력 파일을 HTML 형식으로 저장:

`pygmentize -f html -o {{출력_파일.html}} {{입력_파일.py}}`

- 사용 가능한 출력 형식 목록 표시:

`pygmentize -L formatters`

- 추가 포매터 옵션을 사용하여 HTML 파일 출력 (전체 페이지, 줄 번호 포함):

`pygmentize -f html -O "full,linenos=True" -o {{출력_파일.html}} {{입력_파일}}`
