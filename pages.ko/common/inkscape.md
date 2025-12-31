# inkscape

> SVG (Scalable Vector Graphics) 편집 프로그램.
> Inkscape 버전 0.92.x 이하의 경우, -o 대신 -e를 사용하세요.
> 더 많은 정보: <https://inkscape.org/doc/inkscape-man.html>.

- Inkscape GUI에서 SVG 파일을 열기:

`inkscape {{경로/대상/파일명.svg}}`

- 기본 형식(PNG) 및 기본 해상도(96 DPI)를 사용하여 SVG 파일을 비트맵으로 내보냄:

`inkscape {{경로/대상/파일명.svg}} -o {{경로/대상/파일명.png}}`

- SVG 파일을 600x400 픽셀의 비트맵으로 내보내기 (가로와 세로 사이의 비율 왜곡이 발생할 수 있음):

`inkscape {{경로/대상/파일명.svg}} -o {{경로/대상/파일명.png}} -w {{600}} -h {{400}}`

- SVG 파일의 그림(모든 객체의 경계가 있는 상자)을 비트맵으로 내보냄:

`inkscape {{경로/대상/파일명.svg}} -o {{경로/대상/파일명.png}} -D`

- 해당 ID가 지정된 단일 객체를 비트맵으로 내보냄:

`inkscape {{경로/대상/파일명.svg}} -i {{id}} -o {{object.png}}`

- SVG 문서를 PDF로 내보내고 모든 텍스트를 경로로 변경:

`inkscape {{경로/대상/파일명.svg}} -o {{경로/대상/파일명.pdf}} --export-text-to-path`

- id="path123"로 객체를 복제하고, 복사본을 90도로 회전한 다음, 파일을 저장하고, Inkscape를 종료:

`inkscape {{경로/대상/파일명.svg}} --select=path123 --verb="{{EditDuplicate;ObjectRotate90;FileSave;FileQuit}}"`
