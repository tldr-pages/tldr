# a2ping

> 이미지를 EPS 또는 PDF 파일로 변환.
> 더 많은 정보: <https://manned.org/a2ping>.

- 이미지를 PDF로 변환 (참고: 출력 파일 이름 지정은 선택사항):

`a2ping {{경로/대상/이미지.ext}} {{경로/대상/출력파일.pdf}}`

- 지정된 방법을 사용해 문서를 압축:

`a2ping --nocompress {{none|zip|best|flate}} {{경로/대상/파일}}`

- HiResBoundingBox가 있는 경우 검색 (참고: 기본값은 yes):

`a2ping --nohires {{경로/대상/파일}}`

- 원본 아래 및 왼쪽 페이지 콘텐츠 허용 (참고: 기본값은 no):

`a2ping --below {{경로/대상/파일}}`

- `gs``에 추가 인수 전달:

`a2ping --gsextra {{인수}} {{경로/대상/파일}}`

- 외부 프로그램 (예, pdftops)에 추가 인수 전달:

`a2ping --extra {{인수}} {{경로/대상/파일}}`

- 도움말 표시:

`a2ping -h`
