# ibmcloud ks

> IBM Cloud의 Kubernetes 및 OpenShift 클러스터 관리.
> 더 많은 정보: <https://cloud.ibm.com/docs/cli?topic=cli-kubernetes-service-cli>.

- 클러스터 상세 정보 표시:

`ibmcloud ks cluster get {{[-c|--cluster]}} {{클러스터_아이디}}`

- 클러스터의 인증 기관 인증서 교체 상태 확인:

`ibmcloud ks cluster ca status {{[-c|--cluster]}} {{클러스터_아이디}}`

- 클러스터의 워커 풀 목록 표시:

`ibmcloud ks worker-pool ls {{[-c|--cluster]}} {{클러스터_아이디}}`

- 워커 노드를 삭제하고 동일한 워커 풀에 새 노드로 교체:

`ibmcloud ks worker replace {{[-c|--cluster]}} {{클러스터_아이디}} {{[-w|--worker]}} {{worker_id}}`

- 이 명령에서 사용 가능한 모든 작업 목록 표시:

`ibmcloud ks help`
