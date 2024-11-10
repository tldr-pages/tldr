# pbmtoppa

> PBM 이미지를 HP 프린터 성능 아키텍처 형식으로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtoppa.html>.

- PBM 이미지를 PPA 파일로 변환:

`pbmtoppa {{경로/대상/이미지.pbm}} > {{경로/대상/출력.ppa}}`

- 원하는 인치당 도트 수와 용지 크기 지정:

`pbmtoppa -d {{300}} -s {{a4}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.ppa}}`
