# macptopbm

> MacPaint 파일을 입력으로 받아 PBM 이미지를 출력으로 생성합니다.
> 같이 보기: `pbmtomacp`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/macptopbm.html>.

- MacPaint 파일을 PGM 이미지로 변환:

`macptopbm {{경로/대상/파일.macp}} > {{경로/대상/출력.pbm}}`

- 파일을 읽을 때 지정된 바이트 수만큼 건너뜀:

`macptopbm -extraskip {{N}} > {{경로/대상/출력.pbm}}`

- 모든 정보 메시지 억제:

`macptopbm -quiet > {{경로/대상/출력.pbm}}`

- 버전 표시:

`macptopbm -version`
