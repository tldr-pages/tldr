# pamdeinterlace

> Netpbm 이미지에서 격자 모양으로 행을 제거.
> 같이 보기: `pammixinterlace`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamdeinterlace.html>.

- 입력 이미지의 짝수 행으로 구성된 이미지 생성:

`pamdeinterlace {{경로/대상/이미지.ppm}} > {{경로/대상/출력.ppm}}`

- 입력 이미지의 홀수 행으로 구성된 이미지 생성:

`pamdeinterlace {{[-takeo|-takeodd]}} {{경로/대상/이미지.ppm}} > {{경로/대상/출력.ppm}}`
