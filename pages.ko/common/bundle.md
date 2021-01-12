# bundle

> Ruby 프로그래밍 언어의 종속성 관리자.
> 더 많은 정보: <https://bundler.io/man/bundle.1.html>.

- 작업 디렉토리에 있는 `Gemfile`에 정의된 모든 gem을 설치:

`bundle install`

- `Gemfile` 에 정의된 규칙에 따라 모든 gem을 업데이트 하고 `Gemfile.lock`을 재생성:

`bundle update`

- `Gemfile`에 정의된 특정 gem을 업데이트:

`bundle update --source {{gem명}}`

- 새로운 gem의 스켈레톤 생성:

`bundle gem {{gem명}}`
