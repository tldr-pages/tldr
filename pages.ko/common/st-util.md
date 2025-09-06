# st-util

> STM32 ARM Cortex 마이크로컨트롤러와 상호작용하기 위해 GDB (GNU Debugger) 서버 실행.
> 더 많은 정보: <https://github.com/texane/stlink>.

- 포트 4500에서 GDB 서버 실행:

`st-util -p {{4500}}`

- GDB 서버에 연결:

`(gdb) target extended-remote {{localhost}}:{{4500}}`

- 장치에 펌웨어 쓰기:

`(gdb) load {{firmware.elf}}`
