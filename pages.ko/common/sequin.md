# sequin

> ANSI 이스케이프 시퀀스를 사람이 읽기 쉬운 형태로 변환.
> 터미널 출력을 디버깅하거나, 학습하고 검사할 때 유용.
> 더 많은 정보: <https://github.com/charmbracelet/sequin>.

- 문자열에 포함된 ANSI 이스케이프 시퀀스 설명:

`printf "{{\x1b[38;5;4mCiao, \x1b[1;7mBaby.\x1b[0m\n}}" | sequin`

- 다른 명령의 색상 출력 (예: `ls`) 검사:

`ls -l --color=always | sequin`

- ANSI 시퀀스가 포함된 파일 검사 (예: TUI 골든 파일):

`cat {{경로/대상/파일.golden}} | sequin`

- 가상 TTY에서 명령을 직접 실행하여 출력 검사:

`sequin -- {{ls -l go.*}}`

- 원시 ANSI 시퀀스를 인라인으로 강조하여 쉽게 확인:

`git -c status.color=always status -sb | sequin -r`
