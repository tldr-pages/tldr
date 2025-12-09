# swig

> C/C++ 코드와 JavaScript, Python, C# 등 다양한 고급 언어 간의 바인딩을 생성합니다.
> `.i` 또는 `.swg` 파일을 사용하여 바인딩을 생성하며, SWIG 지시어가 포함된 C/C++ 파일을 출력하여 확장 모듈을 빌드하는 데 필요한 모든 래퍼 코드를 포함합니다.
> 더 많은 정보: <https://www.swig.org/Doc4.4/SWIGDocumentation.html#SWIG_nn2>.

- C++와 Python 간의 바인딩 생성:

`swig -c++ -python -o {{경로/대상/출력_래퍼.cpp}} {{경로/대상/swig_파일.i}}`

- C++와 Go 간의 바인딩 생성:

`swig -go -cgo -intgosize 64 -c++ {{경로/대상/swig_파일.i}}`

- C와 Java 간의 바인딩 생성:

`swig -java {{경로/대상/swig_파일.i}}`

- C와 Ruby 간의 바인딩 생성 및 Ruby 모듈에 `foo::bar::` 접두사 추가:

`swig -ruby -prefix "{{foo::bar::}}" {{경로/대상/swig_파일.i}}`
