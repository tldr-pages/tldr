# berks

> Chef 자세한 설명서 의존 관리자.
> 더 많은 정보: <https://docs.chef.io/berkshelf.html>.

- 로컬 저장소에 자세한 설명서 종속성 설치:

`berks install`

- 특정 자세한 설명서와 그 종속성을 업데이트:

`berks update {{자세한 설명서}}`

- 자세한 설명서를 Chef server에 업로드:

`berks upload {{자세한 설명서}}`

- 자세한 설명서의 종속성 확인:

`berks contingent {{자세한 설명서}}`
