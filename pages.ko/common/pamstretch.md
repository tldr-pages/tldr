# pamstretch

> PAM 이미지를 픽셀 간 보간을 통해 확대.
> 같이 보기: `pamstretch-gen`, `pamenlarge`, `pamscale`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamstretch.html>.

- PAM 이미지를 정수 배율로 확대:

`pamstretch {{n}} {{경로/대상/이미지.pam}} > {{경로/대상/출력.pam}}`

- PAM 이미지를 가로 및 세로 방향으로 지정된 배율로 확대:

`pamstretch {{[-x|-xscale]}} {{xn}} {{[-y|-yscale]}} {{yn}} {{경로/대상/이미지.pam}} > {{경로/대상/출력.pam}}`
