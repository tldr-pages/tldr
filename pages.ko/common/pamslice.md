# pamslice

> PAM 이미지에서 한 줄의 값을 추출.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamslice.html>.

- n번째 행의 픽셀 값을 테이블 형식으로 출력:

`pamslice {{[-r|-row]}} {{n}} {{경로/대상/이미지.pam}}`

- n번째 열의 픽셀 값을 테이블 형식으로 출력:

`pamslice {{[-c|-column]}} {{n}} {{경로/대상/이미지.pam}}`

- 입력 이미지의 m번째 평면만 고려:

`pamslice {{[-r|-row]}} {{n}} -plane {{m}} {{경로/대상/이미지.pam}}`

- 시각화를 위한 `xmgr` 입력 형식으로 출력 생성:

`pamslice {{[-r|-row]}} {{n}} {{[-x|-xmgr]}} {{경로/대상/이미지.pam}}`
