# odps table

> ODPS(Open Data Processing Service)에서 테이블을 생성하고 수정.
> 같이 보기: `odps`.
> 더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 파티션과 수명 주기가 있는 테이블 생성:

`create table {{테이블_이름}} ({{열}} {{타입}}) partitioned by ({{열}} {{타입}}) lifecycle {{일수}};`

- 다른 테이블의 정의를 기반으로 테이블 생성:

`create table {{테이블_이름}} like {{다른_테이블}};`

- 테이블에 파티션 추가:

`alter table {{테이블_이름}} add partition ({{파티션_명세}});`

- 테이블에서 파티션 삭제:

`alter table {{테이블_이름}} drop partition ({{파티션_명세}});`

- 테이블 삭제:

`drop table {{테이블_이름}};`
