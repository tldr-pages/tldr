# pnmquantall

> 여러 파일에 대해 공통 색상표를 사용하여 `pnmquant`를 실행.
> 같이 보기: `pnmquant`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmquantall.html>.

- 지정된 매개 변수로 여러 파일에 `pnmquant`를 실행하여 원본 파일에 덮어쓰기:

`pnmquantall {{색상_수}} {{경로/대상/input1.pnm 경로/대상/input2.pnm ...}}`

- 양자화된 이미지를 입력 파일과 동일한 이름으로 저장하되, 지정된 확장을 추가하여 저장:

`pnmquantall -ext {{확장자}} {{색상_수}} {{경로/대상/input1.pnm 경로/대상/input2.pnm ...}}`
