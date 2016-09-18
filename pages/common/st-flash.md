# st-flash

> Flash binary files to STM32 ARM Cortex microcontrollers.

- Read 4096 bytes of the firmware:

`st-flash read {{firmware.bin}} 0x8000000 4096`

- Write firmware to device:

`st-flash write {{firmware.bin}} 0x8000000`

- Erase firmware from device:

`st-flash erase`
