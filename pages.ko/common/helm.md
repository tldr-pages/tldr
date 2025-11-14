# helm

> Kubernetes 패키지 관리자.
> `install`과 같은 하위 명령어에는 자체 사용법 문서가 있음.
> 더 많은 정보: <https://helm.sh/docs/helm/>.

- helm 차트 생성:

`helm create {{차트_이름}}`

- 새로운 helm 레포지토리를 추가:

`helm repo add {{레포지토리_이름}}`

- helm 레포지토리 나열:

`helm repo list`

- helm 레포지토리 업데이트:

`helm repo update`

- helm 레포지토리 삭제:

`helm repo remove {{레포지토리_이름}}`

- helm 차트 설치:

`helm install {{이름}} {{레포지토리_이름}}/{{차트_이름}}`

- tar 아카이브로 helm 차트 다운로드:

`helm get {{차트_배포_이름}}`

- helm 종속성 업데이트:

`helm dependency update`
