# bosh

> bosh 디렉터를 배치 및 관리하기 위한 커맨드라인 도구.
> 더 많은 정보: <https://bosh.io/docs/cli-v2/>.

- 디렉터의 로컬 별칭 생성:

`bosh alias-env {{환경명}} -e {{ip_주소|url}} --ca-cert {{ca_증명서}}`

- 환경 나열:

`bosh environments`

- 디렉터에 로그인:

`bosh login -e {{환경}}`

- 배포 목록 나열:

`bosh -e {{환경}} deployments`

- 가상 머신 환경 나열:

`bosh -e {{환경}} vms -d {{전개}}`

- 가상 머신의 SSH:

`bosh -e {{환경}} ssh {{가상머신}} -d {{전개}}`

- stemcell 업로드:

`bosh -e {{환경}} upload-stemcell {{stemcell_파일|url}}`

- 현재 클라우드 구성 표시:

`bosh -e {{환경}} cloud-config`
