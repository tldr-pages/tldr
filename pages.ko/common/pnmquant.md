# pnmquant

> PNM 이미지의 색상을 더 작은 세트로 양자화.
> 이 명령은 `pnmcolormap`과 `pnmremap`의 조합이며 `-mapfile`을 제외한 두 명령의 옵션을 모두 허용합니다.
> 같이 보기: `pnmquantall`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmquant.html>.

- 입력 이미지에 최대한 가깝게 `n_colors` 개 이하의 색상만 사용하여 이미지를 생성:

`pnmquant {{n_colors}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`
