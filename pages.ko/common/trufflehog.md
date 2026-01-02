# trufflehog

> 파일, Git 저장소, S3 버킷 및 Docker 이미지에서 인증 정보를 찾고 검증.
> 더 많은 정보: <https://github.com/trufflesecurity/trufflehog#memo-usage>.

- Git 저장소에서 검증된 비밀 검색:

`trufflehog git {{https://github.com/trufflesecurity/test_keys}} --only-verified`

- GitHub 조직에서 검증된 비밀 검색:

`trufflehog github --org {{trufflesecurity}} --only-verified`

- GitHub 저장소에서 검증된 키 검색 및 JSON 출력 받기:

`trufflehog git {{https://github.com/trufflesecurity/test_keys}} --only-verified --json`

- GitHub 저장소와 그 이슈 및 풀 리퀘스트 검색:

`trufflehog github --repo {{https://github.com/trufflesecurity/test_keys}} --issue-comments --pr-comments`

- S3 버킷에서 검증된 키 검색:

`trufflehog s3 --bucket {{버킷 이름}} --only-verified`

- IAM 역할을 사용하여 S3 버킷 검색:

`trufflehog s3 --role-arn {{iam-role-arn}}`

- 개별 파일 또는 디렉터리 검색:

`trufflehog filesystem {{경로/대상/파일_또는_디렉터리1 경로/대상/파일_또는_디렉터리2 ...}}`

- Docker 이미지에서 검증된 비밀 검색:

`trufflehog docker --image {{trufflesecurity/secrets}} --only-verified`
