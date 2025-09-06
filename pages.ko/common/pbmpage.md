# pbmpage

> 인쇄를 위한 테스트 패턴 생성.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmpage.html>.

- US 표준 용지에 인쇄할 테스트 패턴 생성:

`pbmpage > {{경로/대상/파일.pbm}}`

- A4 용지에 인쇄할 테스트 패턴 생성:

`pbmpage -a4 > {{경로/대상/파일.pbm}}`

- 사용할 패턴 지정:

`pbmpage {{1|2|3}} > {{경로/대상/파일.pbm}}`
