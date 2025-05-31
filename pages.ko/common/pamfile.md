# pamfile

> Netpbm (PAM 또는 PNM) 파일 설명.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamfile.html>.

- 지정된 Netpbm 파일 설명:

`pamfile {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 각 입력 파일의 모든 이미지를 설명(각 파일의 첫 번째 이미지만이 아닌 모든 이미지)하고 기계 판독 가능한 형식으로 출력:

`pamfile {{[-a|-allimages]}} -machine {{경로/대상/파일}}`

- 입력 파일에 포함된 이미지 수를 표시:

`pamfile {{[-cou|-count]}} {{경로/대상/파일}}`
