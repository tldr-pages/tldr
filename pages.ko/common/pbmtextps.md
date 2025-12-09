# pbmtextps

> 텍스트를 PostScript를 사용하여 PBM 이미지로 렌더링.
> 같이 보기: `pbmtext`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtextps.html>.

- 한 줄의 텍스트를 PBM 이미지로 렌더링:

`pbmtextps "{{Hello World!}}" > {{경로/대상/출력.pbm}}`

- 폰트와 폰트 크기 지정:

`pbmtextps -font {{Times-Roman}} -fontsize {{30}} "{{Hello World!}}" > {{경로/대상/출력.pbm}}`

- 원하는 좌측 및 상단 여백 지정:

`pbmtextps -leftmargin {{70}} -topmargin {{162}} "{{Hello World!}}" > {{경로/대상/출력.pbm}}`

- 렌더링된 텍스트를 PBM 이미지로 출력하지 않고, 이 이미지를 생성할 PostScript 프로그램으로 출력:

`pbmtextps -dump-ps "{{Hello World!}}" > {{경로/대상/출력.ps}}`
