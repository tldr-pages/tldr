# skaffold

> Kubernetes 애플리케이션의 지속적인 개발을 지원.
> 더 많은 정보: <https://skaffold.dev/docs/references/cli/>.

- 아티팩트 빌드:

`skaffold build -f {{skaffold.yaml}}`

- 코드가 변경될 때마다 앱 빌드 및 배포:

`skaffold dev -f {{skaffold.yaml}}`

- 파이프라인 파일 실행:

`skaffold run -f {{skaffold.yaml}}`

- Skaffold 진단 실행:

`skaffold diagnose -f {{skaffold.yaml}}`

- 아티팩트 배포:

`skaffold deploy -f {{skaffold.yaml}}`
