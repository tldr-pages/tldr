# pio debug

> PlatformIO 프로젝트 디버그.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>.

- 현재 디렉토리의 PlatformIO 프로젝트 디버그:

`pio debug`

- 특정 PlatformIO 프로젝트 디버그:

`pio debug --project-dir {{경로/대상/platformio_project}}`

- 특정 환경 디버그:

`pio debug --environment {{환경}}`

- 특정 설정 파일을 사용하여 PlatformIO 프로젝트 디버그:

`pio debug --project-conf {{경로/대상/platformio.ini}}`

- `gdb` 디버거를 사용하여 PlatformIO 프로젝트 디버그:

`pio debug --interface={{gdb}} {{gdb_옵션}}`
