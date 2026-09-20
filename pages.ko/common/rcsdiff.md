# rcsdiff

> RCS 리비전을 비교하여 RCS 파일의 리비전 간 차이점을 표시.
> 관련 항목: `ci`, `co`, `rcs`, `rlog`.
> 더 많은 정보: <https://manned.org/rcsdiff>.

- 작업 파일과 최신 리비전 비교:

`rcsdiff {{경로/대상/파일}}`

- 작업 파일과 지정한 리비전 비교:

`rcsdiff -r{{리비전}} {{경로/대상/파일}}`

- 파일의 지정한 두 리비전 비교:

`rcsdiff -r{{revision1}} -r{{revision2}} {{경로/대상/파일}}`

- unified 형식으로 차이점 표시:

`rcsdiff -u {{경로/대상/파일}}`

- 문맥 줄을 포함하여 차이점 표시:

`rcsdiff -c {{경로/대상/파일}}`
