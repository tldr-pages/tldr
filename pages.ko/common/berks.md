# berks

> Chef cookbook 의존 관리자. 
> 자세한 정보: <https://docs.chef.io/berkshelf.html>.

- 로컬 저장소에 cookbook 종속성 설치:

`berks install`

- 특정 cookbook과 그 종속성을 업데이트:

`berks update {{cookbook}}`

- cookbook을 Chef server에 업로드:

`berks upload {{cookbook}}`

- cookbook의 종속성 확인:

`berks contingent {{cookbook}}`