# ncdu

> ncurses 인터페이스를 사용하는 디스크 사용량 분석기.
> 더 많은 정보: <https://dev.yorhel.nl/ncdu/man>.

- 현재 작업 중인 디렉터리 분석:

`ncdu`

- 출력에 색상 적용:

`ncdu --color {{dark|off}}`

- 지정된 디렉터리 분석:

`ncdu {{경로/대상/폴더}}`

- 결과를 파일에 저장:

`ncdu -o {{경로/대상/파일}}`

- 패턴과 일치하는 파일 제외(추가 패턴을 위해 여러 번 인수 전달 가능):

`ncdu --exclude '{{*.txt}}'`
