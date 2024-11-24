# pbmtext

> 텍스트를 PBM 이미지로 렌더링.
> 같이 보기: `pbmtextps`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtext.html>.

- 한 줄의 텍스트를 PBM 이미지로 렌더링:

`pbmtext "{{Hello World!}}" > {{경로/대상/출력.pbm}}`

- 여러 줄의 텍스트를 PBM 이미지로 렌더링:

`echo "{{Hello\nWorld!}}" | pbmtext > {{경로/대상/출력.pbm}}`

- PBM 파일로 제공된 사용자 지정 폰트를 사용하여 텍스트 렌더링:

`pbmtext -font {{경로/대상/폰트.pbm}} "{{Hello World!}}" > {{경로/대상/출력.pbm}}`

- 문자와 줄 사이의 픽셀 수 지정:

`echo "{{Hello\nWorld!}}" | pbmtext -space {{3}} -lspace {{10}} > {{경로/대상/출력.pbm}}`
