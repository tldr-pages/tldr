# hexdump

> ASCII, 10진수, 16진수, 8진수 덤프.
> 더 많은 정보: <https://manned.org/hexdump>.

- 파일의 16진수 표현을 출력하고, 중복된 줄을 '\*'로 변경:

`hexdump {{경로/대상/파일}}`

- 입력 오프셋을 16진수로 표시하고 해당 ASCII 표현을 두 열로 표시:

`hexdump {{[-C|--canonical]}} {{경로/대상/파일}}`

- 파일의 16진수 표현을 표시하지만, 입력의 n바이트만 해석:

`hexdump {{[-C|--canonical]}} {{[-n|--length]}} {{바이트_수}} {{경로/대상/파일}}`

- 중복된 줄을 '\*'로 변경하지 않음:

`hexdump {{[-v|--no-squeezing]}} {{경로/대상/파일}}`
