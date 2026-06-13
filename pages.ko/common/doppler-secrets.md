# doppler secrets

> Doppler 프로젝트의 비밀을 관리.
> 더 많은 정보: <https://docs.doppler.com/docs/accessing-secrets>.

- 모든 비밀을 얻기:

`doppler secrets`

- 하나 이상의 비밀 값을 가져오기:

`doppler secrets get {{비밀}}`

- 비밀 파일 업로드:

`doppler secrets upload {{경로/대상/파일.env}}`

- 하나 이상의 비밀 값을 삭제:

`doppler secrets delete {{비밀}}`

- 비밀을 `.env`로 다운로드:

`doppler secrets download --format=env --no-file > {{경로/대상/.env}}`
