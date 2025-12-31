# pamtopng

> PAM 이미지를 PNG로 변환.
> 같이 보기: `pnmtopng`, `pngtopam`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamtopng.html>.

- 지정된 PAM 이미지를 PNG로 변환:

`pamtopng {{경로/대상/이미지.pam}} > {{경로/대상/출력.png}}`

- 출력 이미지에서 지정된 색상을 투명하게 표시:

`pamtopng {{[-t|-transparent]}} {{색상}} {{경로/대상/이미지.pam}} > {{경로/대상/출력.png}}`

- 지정된 파일의 텍스트를 출력물에 tEXt 청크로 포함:

`pamtopng {{[-te|-text]}} {{경로/대상/파일.txt}} {{경로/대상/이미지.pam}} > {{경로/대상/출력.png}}`

- 출력 파일을 Adam7 형식으로 인터레이스 처리:

`pamtopng {{[-in|-interlace]}} {{경로/대상/이미지.pam}} > {{경로/대상/출력.png}}`
