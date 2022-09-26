# aws s3

> AWS S3용 CLI - 웹 서비스 인터페이스를 통해 스토리지를 제공합니다.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- 버킷 안의 파일 보기:

`aws s3 ls {{bucket_name}}`

- 로컬에서 버킷으로 파일 및 디렉토리 동기화:

`aws s3 sync {{path/to/files}} s3://{{bucket_name}}`

- 버킷에서 로컬로 파일 및 디렉토리 동기화:

`aws s3 sync s3://{{bucket_name}} {{path/to/target}}`

- 제외 된 파일 및 디렉토리 동기화:

`aws s3 sync {{path/to/files}} s3://{{bucket_name}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/*`

- 버킷에서 파일 제거:

`aws s3 rm s3://{{bucket}}/{{path/to/file}}`

- 변경 사항만 미리보기:

`aws s3 {{any_command}} --dryrun`
