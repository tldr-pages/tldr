# lilypond

> 악보를 조판하고/또는 파일에서 MIDI를 생성합니다.
> 같이 보기: `musescore`.
> 더 많은 정보: <https://lilypond.org/doc/v2.24/Documentation/usage/command_002dline-usage>.

- lilypond 파일을 PDF로 컴파일:

`lilypond {{경로/대상/파일}}`

- 지정된 형식으로 컴파일:

`lilypond --formats={{형식_덤프}} {{경로/대상/파일}}`

- 진행 상태 업데이트를 생략하고 지정된 파일을 컴파일:

`lilypond -s {{경로/대상/파일}}`

- 지정된 파일을 컴파일하고 출력 파일 이름 지정:

`lilypond --output={{경로/대상/출력_파일}} {{경로/대상/입력_파일}}`

- lilypond의 현재 버전 확인:

`lilypond --version`
