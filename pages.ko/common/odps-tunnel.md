# odps tunnel

> ODPS(Open Data Processing Service)에서의 데이터 터널.
> 같이 보기: `odps`.
> 더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 테이블을 로컬 파일로 다운로드:

`tunnel download {{테이블_이름}} {{경로/대상/파일}};`

- 로컬 파일을 테이블 파티션에 업로드:

`tunnel upload {{경로/대상/파일}} {{테이블_이름}}/{{파티션_사양}};`

- 필드 및 레코드 구분자를 지정하여 테이블 업로드:

`tunnel upload {{경로/대상/파일}} {{테이블_이름}} -fd {{필드_구분자}} -rd {{레코드_구분자}};`

- 여러 스레드를 사용하여 테이블 업로드:

`tunnel upload {{경로/대상/파일}} {{테이블_이름}} -threads {{스레드_수}};`
