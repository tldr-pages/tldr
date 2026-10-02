# terraform init

> Terraform 작업 디렉터리를 초기화하거나 기존 작업 디렉터리를 다시 초기화.
> 더 많은 정보: <https://developer.hashicorp.com/terraform/cli/commands/init>.

- 현재 작업 디렉터리 초기화:

`terraform init`

- 모듈과 프로바이더를 허용되는 최신 버전으로 업그레이드하며 초기화:

`terraform init -upgrade`

- 저장된 설정을 무시하고, 백엔드를 재구성하며 초기화:

`terraform init -reconfigure`

- 기존 상태 마이그레이션을 시도하며, 백엔드를 재구성하고 초기화:

`terraform init -migrate-state`

- 추가 백엔드 설정을 지정하여 초기화:

`terraform init -backend-config '{{키}}={{값}}'`

- 백엔드 또는 HCP Terraform 초기화 없이 초기화:

`terraform init -backend=false`

- 대화형 입력 없이 초기화 (자동화에 유용):

`terraform init -input=false`

- 의존성 잠금 파일을 읽기 전용 모드로 설정해 초기화:

`terraform init -lockfile readonly`
