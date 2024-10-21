# github-label-sync

> GitHub 라벨 동기화.
> 더 많은 정보: <https://github.com/Financial-Times/github-label-sync>.

- 로컬 `labels.json` 파일을 사용하여 라벨을 동기화:

`github-label-sync --access-token {{토큰}} {{레포지토리_이름}}`

- 특정 라벨 JSON 파일을 사용하여 라벨을 동기화:

`github-label-sync --access-token {{토큰}} --labels {{url|경로/대상/json_파일}} {{레포지토리_이름}}`

- 실제로 라벨을 동기화하는 대신 테스트 실행을 수행:

`github-label-sync --access-token {{토큰}} --dry-run {{레포지토리_이름}}`

- `labels.json`에 없는 라벨을 유지:

`github-label-sync --access-token {{토큰}} --allow-added-labels {{레포지토리_이름}}`

- `GITHUB_ACCESS_TOKEN` 환경 변수를 사용하여 동기화:

`github-label-sync {{레포지토리_이름}}`
