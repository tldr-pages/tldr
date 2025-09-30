# ROPgadget

> 바이너리 파일에서 ROP 가젯을 찾습니다.
> 더 많은 정보: <https://github.com/JonathanSalwan/ROPgadget>.

- 바이너리 파일에서 가젯 나열:

`ROPgadget --binary {{경로/대상/바이너리}}`

- 정규 표현식으로 바이너리 파일의 가젯 필터링:

`ROPgadget --binary {{경로/대상/바이너리}} --re {{정규표현식}}`

- 지정된 유형을 제외한 바이너리 파일의 가젯 나열:

`ROPgadget --binary {{경로/대상/바이너리}} --{{norop|nojob|nosys}}`

- 바이너리 파일에서 잘못된 바이트 가젯 제외:

`ROPgadget --binary {{경로/대상/바이너리}} --badbytes {{바이트_문자열}}`

- 지정된 바이트 수까지의 바이너리 파일 가젯 나열:

`ROPgadget --binary {{경로/대상/바이너리}} --depth {{바이트_수}}`
