# biber

> `biblatex` 패키지를 위한 백엔드 참고문헌 처리기.
> 관련 항목: `latexmk`.
> 더 많은 정보: <https://texdoc.org/serve/biber.pdf/0#section.3>.

- BibLaTeX Control File을 사용해 참고문헌 데이터 생성:

`biber {{경로/대상/파일.bcf}}`

- 설정 파일을 사용하여 참고문헌 데이터 생성:

`biber {{경로/대상/파일.bcf}} {{[-g|--configfile]}} {{경로/대상/구성_파일}}`

- 디버깅 활성화:

`biber {{경로/대상/파일.bcf}} {{[-D|--debug]}}`
