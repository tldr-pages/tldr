# bundle

> Ruby 프로그래밍 언어의 종속성 관리자.
> 더 많은 정보: <https://bundler.io/man/bundle.1.html>.

- 작업 디렉토리에 있는 `Gemfile`에 정의된 모든 gem을 설치:

`bundle install`

- 현재 번들의 컨텍스트에서 명령을 실행:

`bundle exec {{명령어}} {{인자}}`

- `Gemfile` 에 정의된 규칙에 따라 모든 gem을 업데이트 하고 `Gemfile.lock`을 재생성:

`bundle update`

- `Gemfile`에 정의된 하나 이상의 특정 gem을 업데이트:

`bundle update {{gem_이름1}} {{gem_이름2}}`

- `Gemfile`에 정의된 하나 이상의 특정 gem을 다음 패치 버전으로만 업데이트:

`bundle update --patch {{gem_이름1}} {{gem_이름2}}`

- `Gemfile`에서 지정된 그룹 내의 모든 gem을 업데이트:

`bundle update --group {{development}}`

- 최신 버전이 있는 `Gemfile`에 설치된 gem을 나열:

`bundle outdated`

- 새로운 gem 스켈레톤을 생성:

`bundle gem {{gem_이름}}`
