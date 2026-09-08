# pulumi config

> Pulumi 스택의 설정을 관리.
> 더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_config/>.

- 현재 설정을 JSON 형식으로 표시:

`pulumi config {{[-j|--json]}}`

- 지정한 스택의 설정 표시:

`pulumi config {{[-s|--stack]}} {{스택_이름}}`

- 지정한 설정 키의 값 조회:

`pulumi config get {{키}}`

- 설정값 제거:

`pulumi config rm {{키}}`

- 파일의 내용을 지정한 설정 키의 값으로 설정:

`cat {{경로/대상/파일}} | pulumi config set {{키}}`

- 설정 키에 비밀값 설정 (예: API 키)하고 암호화된 형태로 저장/표시:

`pulumi config set --secret {{키}} {{S3cr37_값}}`

- 지정한 설정 파일에서 여러 설정값 제거:

`pulumi config --config-file {{경로/대상/파일}} rm-all {{키1 키2 ...}}`
