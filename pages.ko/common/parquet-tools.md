# parquet-tools

> Parquet 파일을 표시하고 검사하며 조작.
> 더 많은 정보: <https://github.com/apache/parquet-mr>.

- Parquet 파일 내용 표시:

`parquet-tools cat {{경로/대상/parquet}}`

- Parquet 파일의 처음 몇 줄 표시:

`parquet-tools head {{경로/대상/parquet}}`

- Parquet 파일의 스키마 출력:

`parquet-tools schema {{경로/대상/parquet}}`

- Parquet 파일의 메타데이터 출력:

`parquet-tools meta {{경로/대상/parquet}}`

- Parquet 파일의 내용과 메타데이터 출력:

`parquet-tools dump {{경로/대상/parquet}}`

- 여러 Parquet 파일을 하나의 대상 파일로 병합:

`parquet-tools merge {{경로/대상/parquet1}} {{경로/대상/parquet2}} {{경로/대상/대상_parquet}}`

- Parquet 파일의 행 수 출력:

`parquet-tools rowcount {{경로/대상/parquet}}`

- Parquet 파일의 열 및 오프셋 색인 출력:

`parquet-tools column-index {{경로/대상/parquet}}`
