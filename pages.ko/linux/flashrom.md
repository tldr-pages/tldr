# flashrom

> 플래시 칩을 읽고, 쓰고, 검증하고, 지웁니다.
> 더 많은 정보: <https://manned.org/flashrom>.

- 칩을 검사하여 배선이 올바른지 확인:

`flashrom --programmer {{프로그래머}}`

- 플래시를 읽고 파일로 저장:

`flashrom -p {{프로그래머}} --read {{경로/대상/파일}}`

- 파일을 플래시에 쓰기:

`flashrom -p {{프로그래머}} --write {{경로/대상/파일}}`

- 플래시를 파일과 대조하여 검증:

`flashrom -p {{프로그래머}} --verify {{경로/대상/파일}}`

- Raspberry Pi를 사용하여 칩 검사:

`flashrom -p {{linux_spi:dev=/dev/spidev0.0}}`
