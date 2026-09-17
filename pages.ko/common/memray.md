# memray

> Python 애플리케이션의 메모리 사용량을 프로파일링하는 도구.
> 더 많은 정보: <https://github.com/bloomberg/memray#usage>.

- Python 파일 실행 중 메모리 사용량 추적:

`memray run {{경로/대상/파일}}.py`

- Python 모듈([m]odule) 실행 중 메모리 사용량 추적:

`memray run -m {{모듈_이름}}`

- 결과 파일 이름 지정:

`memray run {{[-o|--output]}} {{경로/대상/출력_파일}}.bin {{경로/대상/파일}}.py`

- 메모리 사용량 요약 출력:

`memray summary {{경로/대상/파일}}.bin`

- HTML flamegraph 생성:

`memray flamegraph {{경로/대상/파일}}.bin`
