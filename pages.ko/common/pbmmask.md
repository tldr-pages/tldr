# pbmmask

> 일반 비트맵에서 마스크 비트맵 생성.
> 같이 보기: `pambackground`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmmask.html>.

- 배경과 전경을 분리하여 마스크 비트맵 생성:

`pbmmask {{경로/대상/이미지.pbm}} > {{경로/대상/출력.pbm}}`

- 생성된 마스크를 한 픽셀 확장:

`pbmmask -expand {{경로/대상/이미지.pbm}} > {{경로/대상/출력.pbm}}`
