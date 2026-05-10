# dirs_cleaner

> 디렉터리 구조는 유지하고 내부 내용만 재귀적으로 삭제.
> 참고: macOS 13 (Ventura) 이상에선, `dirs_cleaner` AMFI 실행 제한이 있어. `/usr/libexec/dirs_cleaner` 바이너리를 루트를 포함한 사용자 세션에서 직접 실행할 수 없음.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/dirs_cleaner.8.html>.

- 디렉터리 구조는 유지하고 내부 내용만 재귀적으로 삭제:

`sudo dirs_cleaner {{경로/대상/디렉터리1 경로/대상/디렉터리2 ...}}`
