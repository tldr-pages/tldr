# pbmreduce

> PBM 이미지를 비례적으로 축소.
> 같이 보기: `pamenlarge`, `pamditherbw`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmreduce.html>.

- 지정한 이미지를 지정한 비율로 축소:

`pbmreduce {{N}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.pbm}}`

- 단순 임계값을 사용하여 축소:

`pbmreduce -threshold {{N}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.pbm}}`

- 모든 양자화에 지정한 임계값 사용:

`pbmreduce -value {{0.6}} {{N}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.pbm}}`
