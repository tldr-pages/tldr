# quarkus

> Quarkus 프로젝트 생성, 확장 관리 및 기본 빌드 및 개발 작업 수행.
> 더 많은 정보: <https://quarkus.io/guides/cli-tooling>.

- 새 디렉토리에 새 애플리케이션 프로젝트 생성:

`quarkus create app {{프로젝트_명}}`

- 현재 프로젝트를 실시간 코딩 모드로 실행:

`quarkus dev`

- 애플리케이션 실행:

`quarkus run`

- 현재 프로젝트를 지속 테스트 모드로 실행:

`quarkus test`

- 현재 프로젝트에 하나 이상의 확장 추가:

`quarkus extension add {{확장_명1 확장_명2 ...}}`

- Docker를 사용하여 컨테이너 이미지 빌드:

`quarkus image build docker`

- Kubernetes에 애플리케이션 배포:

`quarkus deploy kubernetes`

- 프로젝트 업데이트:

`quarkus update`
