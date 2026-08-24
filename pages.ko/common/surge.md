# surge

> 간단한 웹 게시.
> 더 많은 정보: <https://surge.sh/help/>.

- 새로운 사이트를 surge.sh에 업로드:

`surge {{경로/대상/내_프로젝트}}`

- 사용자 지정 도메인으로 사이트 배포 (DNS 레코드는 surge.sh 하위 도메인을 가리켜야 함):

`surge {{경로/대상/내_프로젝트}} {{내_사용자_도메인.com}}`

- surge 프로젝트 나열:

`surge list`

- 프로젝트 제거:

`surge teardown {{내_사용자_도메인.com}}`
