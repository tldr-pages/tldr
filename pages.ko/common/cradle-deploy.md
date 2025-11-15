# cradle deploy

> Cradle 배포 관리.
> 더 많은 정보: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>.

- 서버에 Cradle을 배포:

`cradle deploy production`

- 아마존 S3에 정적 자산 배포:

`cradle deploy s3`

- Yarn "components" 디렉토리를 포함하여 정적 자산 배포:

`cradle deploy s3 --include-yarn`

- "upload" 디렉토리를 포함한 정적 자산 배포:

`cradle deploy s3 --include-upload`
