# gnatmake

> Ada 프로그램용 저수준 빌드 도구 (GNAT 도구 체인의 일부).
> 더 많은 정보: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Switches-for-gnatmake.html>.

- 실행 파일을 컴파일:

`gnatmake {{소스_파일1.adb 소스_파일2.adb ...}}`

- 사용자 정의 실행 파일 이름을 설정:

`gnatmake -o {{실행파일_이름}} {{소스_파일.adb}}`

- 강제([f]orce) 재컴파일:

`gnatmake -f {{소스_파일.adb}}`
