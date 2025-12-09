# kosmorro

> 특정 날짜 및 지구상의 위치에 대한 천체력 및 이벤트를 계산.
> 더 많은 정보: <https://github.com/Kosmorro/kosmorro/blob/master/manpage/kosmorro.1.md>.

- 프랑스 파리의 천체력 얻기:

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}}`

- UTC+2 시간대의 프랑스 파리의 천체력 얻기:

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --timezone={{2}}`

- 2020년 6월 9일의 프랑스 파리의 천체력 얻기:

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --date={{2020-06-09}}`

- PDF 생성 (참고: TeXLive가 설치되어 있어야 함):

`kosmorro --format={{pdf}} --output={{경로/대상/파일.pdf}}`
