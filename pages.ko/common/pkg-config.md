# pkg-config

> 애플리케이션 컴파일을 위한 설치된 라이브러리의 세부 정보를 제공.
> 더 많은 정보: <https://manned.org/pkg-config>.

- 라이브러리 및 그 의존성 목록 확인:

`pkg-config --libs {{라이브러리1 라이브러리2 ...}}`

- 라이브러리, 그 의존성 및 gcc에 대한 적절한 cflags 목록 확인:

`pkg-config --cflags --libs {{라이브러리1 라이브러리2 ...}}`

- libgtk-3, libwebkit2gtk-4.0 및 모든 의존성을 사용하여 코드 컴파일:

`c++ example.cpp $(pkg-config --cflags --libs gtk+-3.0 webkit2gtk-4.0) -o example`
