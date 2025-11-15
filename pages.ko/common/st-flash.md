# st-flash

> STM32 ARM Cortex 마이크로컨트롤러에 바이너리 파일을 플래시.
> 더 많은 정보: <https://manned.org/st-flash>.

- 장치에서 0x8000000부터 4096 바이트 읽기:

`st-flash read {{펌웨어}}.bin {{0x8000000}} {{4096}}`

- 장치에 0x8000000부터 펌웨어 쓰기:

`st-flash write {{펌웨어}}.bin {{0x8000000}}`

- 장치에서 펌웨어 지우기:

`st-flash erase`
