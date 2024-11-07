# engrampa

> MATE 데스크톱 환경에서 zip/tar 파일로 패키지 파일을 압축.
> 같이 보기: `zip`, `tar`.
> 더 많은 정보: <https://github.com/mate-desktop/engrampa>.

- Engrampa 시작:

`engrampa`

- 특정 압축 파일 열기:

`engrampa {{경로/대상/압축파일1.tar 경로/대상/압축파일2.tar ...}}`

- 특정 파일 및/또는 폴더를 재귀적으로 압축:

`engrampa --add-to={{경로/대상/압축된.tar}} {{경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...}}`

- 압축 파일에서 파일 및/또는 폴더를 특정 경로로 추출:

`engrampa --extract-to={{경로/대상/폴더}} {{경로/대상/압축파일1.tar 경로/대상/압축파일2.tar ...}}`
