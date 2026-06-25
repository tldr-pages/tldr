# minipro

> Xgecu 칩 프로그래머 (TL866A/CS, TL866II+, T48, T56) 제어 도구.
> AVR, PIC, 마이크로컨트롤러 및 메모리 등 다양한 칩 지원.
> 더 많은 정보: <https://manned.org/minipro>.

- 지원되는 모든 장치 목록 표시:

`minipro {{[-l|--list]}}`

- 특정 장치 검색:

`minipro {{[-L|--search]}} {{장치_이름}}`

- 칩 ID 읽기:

`minipro {{[-p|--device]}} {{칩_이름}} {{[-D|--read_id]}}`

- 칩 내용을 파일로 읽기:

`minipro {{[-p|--device]}} {{칩_이름}} {{[-r|--read]}} {{경로/대상/출력_파일.bin}}`

- 파일 내용을 칩에 기록:

`minipro {{[-p|--device]}} {{칩_이름}} {{[-w|--write]}} {{경로/대상/입력_파일.bin}}`

- 칩 내용과 파일 비교:

`minipro {{[-p|--device]}} {{칩_이름}} {{[-m|--verify]}} {{경로/대상/파일.bin}}`

- 칩 지우기:

`minipro {{[-p|--device]}} {{칩_이름}} {{[-E|--erase]}}`

- 도움말 표시:

`minipro {{[-h|--help]}}`
