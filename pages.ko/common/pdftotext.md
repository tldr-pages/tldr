# pdftotext

> PDF 파일을 일반 텍스트 형식으로 변환.
> 더 많은 정보: <https://www.xpdfreader.com/pdftotext-man.html>.

- `filename.pdf`를 일반 텍스트로 변환하고 `stdout`에 출력:

`pdftotext {{filename.pdf}} -`

- `filename.pdf`를 일반 텍스트로 변환하고 `filename.txt`로 저장:

`pdftotext {{filename.pdf}}`

- `filename.pdf`를 일반 텍스트로 변환하고 레이아웃 유지:

`pdftotext -layout {{filename.pdf}}`

- `input.pdf`를 일반 텍스트로 변환하고 `output.txt`로 저장:

`pdftotext {{input.pdf}} {{output.txt}}`

- `input.pdf`의 2, 3, 4 페이지를 일반 텍스트로 변환하고 `output.txt`로 저장:

`pdftotext -f {{2}} -l {{4}} {{input.pdf}} {{output.txt}}`
