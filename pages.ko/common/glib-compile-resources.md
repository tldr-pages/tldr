# glib-compile-resources

> 리소스 파일 (예: 이미지)을 바이너리 리소스 번들로 컴파일.
> GResource API를 사용해 GTK 애플리케이션에 연결될 수 있음.
> 더 많은 정보: <https://manned.org/glib-compile-resources>.

- `file.gresource.xml`에서 참조된 리소스를 .gresource 바이너리로 컴파일:

`glib-compile-resources {{파일.gresource.xml}}`

- `file.gresource.xml`에서 참조된 리소스를 C 소스 파일로 컴파일:

`glib-compile-resources --generate-source {{파일.gresource.xml}}`

- `file.gresource.xml`의 리소스를 `.c`, `.h` 또는 `.gresource` 확장자를 사용하여 선택한 대상 파일로 컴파일:

`glib-compile-resources --generate --target={{file.ext}} {{파일.gresource.xml}}`

- `file.gresource.xml`에서 참조되는 리소스 파일 목록을 출력:

`glib-compile-resources --generate-dependencies {{파일.gresource.xml}}`
