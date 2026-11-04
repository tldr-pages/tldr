# webpmux

> WebP 애니메이션 생성.
> 더 많은 정보: <https://developers.google.com/speed/webp/docs/webpmux>.

- 2개의 프레임으로 애니메이션 생성:

`webpmux -frame {{경로/대상/프레임1.webp}} +{{500}} -frame {{경로/대상/프레임2.webp}} +{{500}} -loop {{0}} -o {{경로/대상/출력파일.webp}}`
