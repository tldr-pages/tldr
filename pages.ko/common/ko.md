# ko

> Kubernetes에서 Go 애플리케이션을 컨테이너 이미지로 빌드하고 배포.
> 더 많은 정보: <https://ko.build/reference/ko/>.

- Go 패키지 import 경로로부터 컨테이너 이미지 빌드 및 게시:

`ko build {{import_경로}}`

- 컨테이너 이미지를 빌드해, 로컬 Docker 데몬에 로드:

`ko build {{[-L|--local]}} {{import_경로}}`

- Go 이미지 참조를 digest로 변환하여 Kubernetes 매니페스트 적용:

`ko apply {{[-f|--filename]}} {{경로/대상/매니페스트.yaml}}`

- 이미지 참조가 변환된 Kubernetes 리소스 생성:

`ko create {{[-f|--filename]}} {{경로/대상/매니페스트.yaml}}`

- Kubernetes 매니페스트를 적용하지 않고 변환 결과만 출력:

`ko resolve {{[-f|--filename]}} {{경로/대상/매니페스트.yaml}}`

- Go 패키지를 빌드해서 Kubernetes에서 실행:

`ko run {{import_경로}}`

- 매니페스트에 정의된 Kubernetes 리소스 삭제:

`ko delete {{[-f|--filename]}} {{경로/대상/매니페스트.yaml}}`

- 컨테이너 레지스트리에 로그인:

`ko login {{registry.example.com}} {{[-u|--username]}} {{사용자명}} {{[-p|--password]}} {{비밀번호}}`
