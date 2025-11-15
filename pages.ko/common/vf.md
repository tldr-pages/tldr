# vf

> VirtualFish는 Python 가상 환경을 관리하기 위한 fish shell 도구입니다.
> 더 많은 정보: <https://virtualfish.readthedocs.io/en/latest/>.

- 가상 환경 생성:

`vf new {{가상환경_이름}}`

- 특정 Python 버전으로 가상 환경 생성:

`vf new --python {{/usr/local/bin/python3.8}} {{가상환경_이름}}`

- 지정한 가상 환경 활성화 및 사용:

`vf activate {{가상환경_이름}}`

- 현재 가상 환경을 현재 디렉토리에 연결하여 들어가면 자동으로 활성화하고 나가면 자동으로 비활성화:

`vf connect`

- 현재 가상 환경 비활성화:

`vf deactivate`

- 모든 가상 환경 나열:

`vf ls`

- 가상 환경 제거:

`vf rm {{가상환경_이름}}`

- 도움말 표시:

`vf help`
