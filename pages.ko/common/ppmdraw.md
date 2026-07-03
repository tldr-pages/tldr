# ppmdraw

> 스크립트를 실행하여 PPM 이미지에 선, 텍스트 등을 그림.
> 사용되는 스크립트 언어에 대한 문서는 아래 링크에서 확인 가능.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmdraw.html>.

- 지정한 스크립트를 실행하여 PPM 이미지에 그리기:

`ppmdraw -script '{{setpos 50 50; text_here "hello!"; }}' {{경로/대상/이미지.pnm}} > {{경로/대상/출력파일.pnm}}`

- 지정한 스크립트 파일을 실행하여 PPM 이미지에 그리기:

`ppmdraw -scriptfile {{경로/대상/스크립트}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력파일.pnm}}`
