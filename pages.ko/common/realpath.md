# realpath

> 파일이나 디렉터리에 대한 절대 경로를 표시.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html>.

- 파일이나 디렉터리에 대한 절대 경로 표시:

`realpath {{경로/대상/파일_또는_폴더}}`

- 모든 경로 구성 요소가 존재해야 함:

`realpath {{[-e|--canonicalize-existing]}} {{경로/대상/파일_또는_폴더}}`

- 심볼릭 링크 전에 ".." 구성 요소 해결:

`realpath {{[-L|--logical]}} {{경로/대상/파일_또는_폴더}}`

- 심볼릭 링크 확장 비활성화:

`realpath {{[-s|--no-symlinks]}} {{경로/대상/파일_또는_폴더}}`

- 오류 메시지 억제:

`realpath {{[-q|--quiet]}} {{경로/대상/파일_또는_폴더}}`
