# ctr

> `containerd` 컨테이너 및 이미지 관리.
> 더 많은 정보: <https://manned.org/ctr>.

- 모든 컨테이너 나열 (실행 중 및 중지됨):

`ctr containers list`

- 모든 이미지 나열:

`ctr images list`

- 이미지 다운로드:

`ctr images pull {{이미지}}`

- 이미지 태그 지정:

`ctr images tag {{소스_이미지}}:{{소스_태그}} {{대상_이미지}}:{{대상_태그}}`
