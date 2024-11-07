# lpinfo

> CUPS 프린트 서버의 연결된 프린터 및 설치된 드라이버 나열.
> 더 많은 정보: <https://openprinting.github.io/cups/doc/man-lpinfo.html>.

- 현재 연결된 모든 프린터 나열:

`lpinfo -v`

- 현재 설치된 모든 프린터 드라이버 나열:

`lpinfo -m`

- 제조사 및 모델로 설치된 프린터 드라이버 검색:

`lpinfo --make-and-model "{{프린터_모델}}" -m`
