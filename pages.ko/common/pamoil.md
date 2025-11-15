# pamoil

> PAM 이미지를 유화로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamoil.html>.

- PAM 이미지를 유화로 변환:

`pamoil {{경로/대상/입력_파일.pam}} > {{경로/대상/출력_파일.pam}}`

- "번지기" 효과를 위해 N 픽셀의 이웃을 고려:

`pamoil -n {{n}} {{경로/대상/입력_파일.pam}} > {{경로/대상/출력_파일.pam}}`
