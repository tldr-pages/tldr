# dtc

> 장치 트리 컴파일러는 형식 간에 장치 트리를 다시 컴파일하는 도구.
> 더 많은 정보: <https://github.com/dgibson/dtc>.

- `.dtb` 파일을 읽을 수 있는 `.dts` 파일로 디컴파일:

`dtc -I dtb -O dts -o {{경로/대상/출력_파일.dts}} {{경로/대상/입력_파일.dtb}}`
