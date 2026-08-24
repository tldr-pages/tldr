# ipaggmanip

> `ipaggcreate`로 생성된 집계 통계를 가공하는 도구.
> 더 많은 정보: <https://manned.org/ipaggmanip>.

- 상위 비트가 동일한 라벨을 결합:

`ipaggmanip {{[-p|--prefix]}} {{16}} {{경로/대상/파일}}`

- 지정한 바이트 수보다 작은 카운트를 가진 라벨 제거 및 일부 라벨 샘플링:

`ipaggmanip --cut-smaller {{100}} --cull-labels {{5}} {{경로/대상/파일}}`

- 0이 아닌 카운트를 모두 1로 반환:

`ipaggmanip {{[-P|--posterize]}} {{경로/대상/파일}}`
