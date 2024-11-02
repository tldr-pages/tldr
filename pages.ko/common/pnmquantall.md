# pnmquantall

> 여러 파일에 대해 `pnmquant`를 실행하여 공통 색상 지도를 공유하도록 합니다.
> 같이 보기: `pnmquant`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmquantall.html>.

- 지정된 매개변수로 여러 파일에서 `pnmquant` 실행 후 원본 파일을 덮어쓰기:

`pnmquantall {{색상_수}} {{경로/대상/입력1.pnm 경로/대상/입력2.pnm ...}}`

- 양자화된 이미지를 입력 파일과 동일한 이름으로 저장하되, 지정된 확장자를 추가하여 저장:

`pnmquantall -ext {{확장자}} {{색상_수}} {{경로/대상/입력1.pnm 경로/대상/입력2.pnm ...}}`
