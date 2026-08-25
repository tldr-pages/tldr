# scdoc

> `man` 매뉴얼 페이지를 생성.
> 더 많은 정보: <https://git.sr.ht/~sircmpwn/scdoc/tree/master/item/scdoc.1.scd>.

- scdoc (`.scd`) 파일에서 man 페이지 생성:

`scdoc < {{경로/대상/파일.scd}} > {{경로/대상/파일.1}}`

- scdoc 파일에서 man 페이지 생성 후 생성된 troff (man) 소스 표시:

`scdoc < {{경로/대상/파일.scd}} | {{less}}`
