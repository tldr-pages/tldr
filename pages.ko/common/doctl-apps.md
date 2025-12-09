# doctl apps

> DigitalOcean 앱 관리.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/apps>.

- 애플리케이션 생성:

`doctl apps create`

- 특정 애플리케이션에 대한 배포 생성:

`doctl apps create-deployment {{앱_아이디}}`

- 대화형으로 앱 삭제:

`doctl apps delete {{앱_아이디}}`

- 앱 다운로드:

`doctl apps get`

- 모든 앱 나열:

`doctl apps list`

- 특정 앱의 모든 배포를 나열:

`doctl apps list-deployments {{앱_아이디}}`

- 특정 앱에서 로그를 가져오기:

`doctl apps logs {{앱_아이디}}`

- 특정 앱 사양으로 특정 앱을 업데이트:

`doctl apps update {{앱_아이디}} --spec {{path/to/spec.yml}}`
