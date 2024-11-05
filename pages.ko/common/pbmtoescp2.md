# pbmtoescp2

> PBM 이미지를 ESC/P2 프린터 파일로 변환.
> 같이 보기: `pbmtoepson`, `escp2topbm`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtoescp2.html>.

- PBM 이미지를 ESC/P2 프린터 파일로 변환:

`pbmtoescp2 {{경로/대상/이미지.pbm}} > {{경로/대상/출력.escp2}}`

- 출력의 압축 지정:

`pbmtoescp2 -compression {{0|1}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.escp2}}`

- 출력을 인치당 도트 수로 가로 및 세로 해상도 지정:

`pbmtoescp2 -resolution {{180|360|720}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.escp2}}`

- 출력의 끝에 폼피드 명령 추가:

`pbmtoescp2 -formfeed {{경로/대상/이미지.pbm}} > {{경로/대상/출력.escp2}}`
