# sh5util

> `sacct_gather_profile` 플러그인이 생성한 HDF5 파일 병합 도구.
> 더 많은 정보: <https://slurm.schedmd.com/sh5util.html>.

- 지정된 작업 또는 단계에 대해 각 할당된 노드에서 생성된 HDF5 파일 병합:

`sh5util --jobs={{작업_ID|작업_ID.단계_ID}}`

- 병합된 작업 파일에서 하나 이상의 데이터 시리즈 추출:

`sh5util --jobs={{작업_ID|작업_ID.단계_ID}} --extract -i {{경로/대상/파일.h5}} --series={{Energy|Filesystem|Network|Task}}`

- 병합된 작업 파일에서 모든 노드의 하나의 데이터 항목 추출:

`sh5util --jobs={{작업_ID|작업_ID.단계_ID}} --item-extract --series={{Energy|Filesystem|Network|Task}} --data={{데이터_항목}}`
