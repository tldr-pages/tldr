# loft

> 가상 클러스터를 사용하여 멀티테넌트 Kubernetes 환경 설치 및 관리.
> 더 많은 정보: <https://loft.sh/docs/cli/loft/>.

- 현재 Kubernetes 클러스터에 Loft 설치 또는 업그레이드:

`loft start`

- 원격 Loft 인스턴스에 로그인:

`loft login {{https://loft.example.com}}`

- 특정 스페이스와 클러스터에 가상 클러스터 생성:

`loft create vcluster {{가상클러스터_이름}} {{[-s|--space]}} {{스페이스_이름}} {{[-c|--cluster]}} {{클러스터_이름}}`

- 모든 가상 클러스터 목록 조회:

`loft list vclusters`

- 특정 가상 클러스터로 컨텍스트 전환:

`loft use vcluster {{가상클러스터_이름}}`

- 가상 클러스터 삭제:

`loft delete vcluster {{가상클러스터_이름}}`

- 현재 Loft 사용자 이름을 확인:

`loft vars username`

- 클러스터에서 Loft 제거:

`loft uninstall`
