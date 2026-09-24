# uv publish

> 배포 패키지를 패키지 인덱스에 업로드.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-publish>.

- `dist/` 디렉터리의 패키지 배포 (기본 동작):

`uv publish`

- 지정한 저장소 URL에 패키지 배포:

`uv publish --publish-url {{https://upload.pypi.org/legacy/}}`

- 지정한 사용자 이름과 비밀번호를 사용하여 패키지 배포:

`uv publish {{[-u|--username]}} {{사용자명}} {{[-p|--password]}} {{비밀번호}}`

- API 토큰을 사용하여 패키지 배포:

`uv publish {{[-t|--token]}} {{사용자_api_토큰}}`

- 지정한 배포 파일 배포:

`uv publish {{경로/대상/목적지/*.whl}} {{경로/대상/목적지/*.tar.gz}}`

- 테스트를 위해 TestPyPI에 패키지 배포:

`uv publish --publish-url https://test.pypi.org/legacy/`
