# lpr

> 파일을 인쇄합니다.
> 같이 보기: `lpstat` 및 `lpadmin`.
> 더 많은 정보: <https://openprinting.github.io/cups/doc/man-lpr.html>.

- 기본 프린터로 파일 인쇄:

`lpr {{경로/대상/파일}}`

- 2부 인쇄:

`lpr -# {{2}} {{경로/대상/파일}}`

- 지정된 프린터로 인쇄:

`lpr -P {{프린터}} {{경로/대상/파일}}`

- 특정 페이지(예: 2) 또는 페이지 범위(예: 2-16) 인쇄:

`lpr -o page-ranges={{2|2-16}} {{경로/대상/파일}}`

- 세로(긴) 또는 가로(짧은) 양면 인쇄:

`lpr -o sides={{two-sided-long-edge|two-sided-short-edge}} {{경로/대상/파일}}`

- 페이지 크기 설정 (설정에 따라 더 많은 옵션 사용 가능):

`lpr -o media={{a4|letter|legal}} {{경로/대상/파일}}`

- 한 장에 여러 페이지 인쇄:

`lpr -o number-up={{2|4|6|9|16}} {{경로/대상/파일}}`
