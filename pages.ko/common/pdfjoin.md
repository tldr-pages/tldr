# pdfjoin

> pdfjam을 기반으로 한 PDF 병합 도구.
> 더 많은 정보: <https://github.com/rrthomas/pdfjam-extras>.

- 두 개의 PDF를 기본 접미사 "joined"로 하나로 병합:

`pdfjoin {{경로/대상/파일1.pdf}} {{경로/대상/파일2.pdf}}`

- 각 파일의 첫 번째 페이지를 함께 병합:

`pdfjoin {{경로/대상/파일1.pdf 경로/대상/파일2.pdf ...}} {{1}} --outfile {{출력_파일}}`

- 페이지 3에서 5까지와 페이지 1을 순서대로 새로운 PDF로 저장하고 사용자 정의 접미사를 추가:

`pdfjoin {{경로/대상/파일.pdf}} {{3-5,1}} --suffix {{재정렬했음}}`

- 두 PDF의 페이지 하위 범위를 병합:

`pdfjoin {{경로/대상/파일1.pdf}} {{2-}} {{파일2}} {{last-3}} --outfile {{출력_파일}}`
