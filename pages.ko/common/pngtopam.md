# pngtopam

> PNG 이미지를 Netpbm 이미지로 변환.
> 같이 보기: `pamtopng`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pngtopam.html>.

- 지정된 PNG 이미지를 Netpbm 이미지로 변환:

`pngtopam {{경로/대상/이미지.png}} > {{경로/대상/출력.pam}}`

- 입력 이미지의 주 이미지와 투명 마스크를 포함한 출력 이미지 생성:

`pngtopam -alphapam {{경로/대상/이미지.png}} > {{경로/대상/출력.pam}}`

- 투명한 픽셀을 지정된 색상으로 대체:

`pngtopam {{[-m|-mix]}} {{[-ba|-background]}} {{색상}} {{경로/대상/이미지.png}} > {{경로/대상/출력.pam}}`

- 입력 이미지에서 발견된 tEXt 청크를 지정된 텍스트 파일로 작성:

`pngtopam {{[-te|-text]}} {{경로/대상/파일.txt}} {{경로/대상/이미지.png}} > {{경로/대상/출력.pam}}`
