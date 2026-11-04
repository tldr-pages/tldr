# rails new

> 새로운 Rails 애플리케이션을 생성.
> 더 많은 정보: <https://guides.rubyonrails.org/command_line.html#rails-new>.

- 현재 디렉터리에 `blog`라는 이름의 Rails 애플리케이션 생성:

`rails new blog`

- API 전용 구성으로 Rails 애플리케이션 생성:

`rails new {{애플리케이션_이름}} --api`

- 데이터베이스로 `postgresql`을 사용하는 Rails 애플리케이션 생성:

`rails new {{애플리케이션_이름}} {{[-d|--database]}} postgresql`

- JavaScript 파일을 생성하지 않고 Rails 애플리케이션 생성:

`rails new {{애플리케이션_이름}} {{[-J|--skip-javascript]}}`

- 도움말 표시:

`rails new {{[-h|--help]}}`
