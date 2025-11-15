# helm install

> helm 차트 설치.
> 더 많은 정보: <https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package>.

- helm 차트 설치:

`helm install {{이름}} {{레포지토리_이름}}/{{차트_이름}}`

- 압축을 푼 차트 디렉터리에서 helm 차트를 설치:

`helm install {{이름}} {{경로/대상/소스_디렉터리}}`

- URL에서 helm 차트를 설치:

`helm install {{패키지_이름}} {{https://example.com/charts/packagename-1.2.3.tgz}}`

- helm 차트 설치하고 이름을 생성:

`helm install {{레포지토리_이름}}/{{차트_이름}} --generate-name`

- 연습 실행을 수행:

`helm install {{이름}} {{레포지토리_이름}}/{{차트_이름}} --dry-run`

- Install a helm chart with custom values:

`helm install {{이름}} {{레포지토리_이름}}/{{차트_이름}} --set {{매개변수1}}={{값1}},{{매개변수2}}={{값2}}`

- 사용자 정의 값 파일을 전달하는 helm 차트를 설치:

`helm install {{이름}} {{레포지토리_이름}}/{{차트_이름}} --values {{경로/대상/값들.yaml}}`
