# fiascotopnm

> 압축된 FIASCO 파일을 PNM 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/fiascotopnm.html>.

- 압축된 FIASCO 파일을 PNM 파일로 변환하거나 비디오 스트리밍의 경우 여러 PNM 파일을 변환:

`fiascotopnm {{경로/대상/파일.fiasco}} -o {{출력_파일_기본이름}}`

- 빠른 압축 풀기를 사용하면, 출력 파일의 품질이 약간 저하됨:

`fiascotopnm --fast {{경로/대상/파일.fiasco}} -o {{출력_파일_기본이름}}`

- 지정된 구성 파일에서 사용할 옵션을 로드:

`fiascotopnm --config {{경로/대상/fiascorc}} {{경로/대상/파일.fiasco}} -o {{출력_파일_기본이름}}`

- 압축 해제된 이미지를 2^n배로 확대:

`fiascotopnm --magnify {{n}} {{경로/대상/파일.fiasco}} -o {{출력_파일_기본이름}}`

- 지정된 양만큼 압축 해제된 이미지를 부드럽게 함:

`fiascotopnm --smooth {{n}} {{경로/대상/파일.fiasco}} -o {{출력_파일_기본이름}}`
