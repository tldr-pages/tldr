# verilator

> Verilog 및 SystemVerilog 하드웨어 설명 언어(HDL) 디자인을 C++ 또는 SystemC 모델로 변환하여 컴파일 후 실행.
> 더 많은 정보: <https://veripool.org/guide/latest/>.

- 현재 디렉토리에서 특정 C 프로젝트 빌드:

`verilator --binary --build-jobs 0 -Wall {{경로/대상/소스.v}}`

- 특정 폴더에 C++ 실행 파일 생성:

`verilator --cc --exe --build --build-jobs 0 -Wall {{경로/대상/소스.cpp}} {{경로/대상/출력.v}}`

- 현재 디렉토리의 코드에 대해 린팅 수행:

`verilator --lint-only -Wall`

- 디자인에 대한 XML 출력 생성(파일, 모듈, 인스턴스 계층 구조, 논리 및 데이터 유형)하여 다른 도구에 입력:

`verilator --xml-output -Wall {{경로/대상/출력.xml}}`
