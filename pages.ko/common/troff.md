# troff

> groff (GNU Troff) 문서 형식 시스템을 위한 조판 프로세서.
> 같이 보기: `groff`.
> 더 많은 정보: <https://manned.org/troff>.

- 출력 형식을 PostScript 프린터용으로 지정하고, 출력을 파일에 저장:

`troff {{경로/대상/입력.roff}} | grops > {{경로/대상/출력.ps}}`

- [me] 매크로 패키지를 사용하여 출력 형식을 PostScript 프린터용으로 지정하고, 출력을 파일에 저장:

`troff -{{me}} {{경로/대상/입력.roff}} | grops > {{경로/대상/출력.ps}}`

- 출력 형식을 [a]SCII 텍스트로 지정하고 [man] 매크로 패키지를 사용:

`troff -T {{ascii}} -{{man}} {{경로/대상/입력.roff}} | grotty`

- 출력 형식을 [pdf] 파일로 지정하고, 출력을 파일에 저장:

`troff -T {{pdf}} {{경로/대상/입력.roff}} | gropdf > {{경로/대상/출력.pdf}}`
