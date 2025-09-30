# pamtogif

> Netpbm 이미지를 애니메이션이 없는 GIF 이미지로 변환.
> 같이 보기: `giftopnm`, `gifsicle`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamtogif.html>.

- Netpbm 이미지를 애니메이션이 없는 GIF 이미지로 변환:

`pamtogif {{경로/대상/이미지.pam}} > {{경로/대상/출력.gif}}`

- 출력 GIF 파일에서 지정한 색상을 투명하게 설정:

`pamtogif {{[-t|-transparent]}} {{색상}} {{경로/대상/이미지.pam}} > {{경로/대상/출력.gif}}`

- 출력 GIF 파일에 지정한 텍스트를 주석으로 포함:

`pamtogif {{[-c|-comment]}} "{{Hello World!}}" {{경로/대상/이미지.pam}} > {{경로/대상/출력.gif}}`
