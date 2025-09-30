# pambrighten

> PAM 이미지의 채도와 명도를 변경.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pambrighten.html>.

- 각 픽셀의 채도를 지정된 백분율만큼 증가:

`pambrighten {{[-s|-saturation]}} {{백분율_값}} {{경로/대상/이미지.pam}} > {{경로/대상/출력.pam}}`

- 각 픽셀의 명도(HSV 색상 공간에서)를 지정된 백분율만큼 증가:

`pambrighten {{[-va|-value]}} {{백분율_값}} {{경로/대상/이미지.pam}} > {{경로/대상/출력.pam}}`
