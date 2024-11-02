# pbmtoascii

> PBM 이미지를 ASCII 그래픽으로 변환.
> 같이 보기: `ppmtoascii`, `asciitopgm`, `ppmtoterm`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtoascii.html>.

- PBM 파일을 입력으로 받고 ASCII 출력 생성:

`pbmtoascii {{경로/대상/입력_파일.pbm}}`

- PBM 파일을 입력으로 받고 ASCII 출력을 파일로 저장:

`pbmtoascii {{경로/대상/입력_파일.pbm}} > {{경로/대상/출력_파일}}`

- 픽셀 매핑을 설정하여 PBM 파일을 입력으로 받기 (기본값은 1x2):

`pbmtoascii -{{1x2|2x4}} {{경로/대상/입력_파일.pbm}}`

- 버전 표시:

`pbmtoascii -version`
