# stolonctl

> Stolon의 CLI, PostgreSQL 고가용성을 위한 클라우드 네이티브 PostgreSQL 관리자.
> 더 많은 정보: <https://github.com/sorintlab/stolon>.

- 클러스터 상태 확인:

`stolonctl --cluster-name {{클러스터_이름}} --store-backend {{스토어_백엔드}} --store-endpoints {{스토어_엔드포인트}} status`

- 클러스터 데이터 가져오기:

`stolonctl --cluster-name {{클러스터_이름}} --store-backend {{스토어_백엔드}} --store-endpoints {{스토어_엔드포인트}} clusterdata`

- 클러스터 사양 가져오기:

`stolonctl --cluster-name {{클러스터_이름}} --store-backend {{스토어_백엔드}} --store-endpoints {{스토어_엔드포인트}} spec`

- JSON 형식의 패치를 사용하여 클러스터 사양 업데이트:

`stolonctl --cluster-name {{클러스터_이름}} --store-backend {{스토어_백엔드}} --store-endpoints {{스토어_엔드포인트}} update --patch '{{클러스터_사양}}'`
