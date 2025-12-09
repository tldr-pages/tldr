# rails generate

> 기존 프로젝트에서 새로운 Rails 템플릿 생성.
> 더 많은 정보: <https://guides.rubyonrails.org/command_line.html#bin-rails-generate>.

- 사용 가능한 모든 생성기 나열:

`rails generate`

- 제목과 본문 속성을 가진 Post라는 새로운 모델 생성:

`rails generate model {{Post}} {{title:string}} {{body:text}}`

- index, show, new, create 액션을 가진 Posts라는 새로운 컨트롤러 생성:

`rails generate controller {{Posts}} {{index}} {{show}} {{new}} {{create}}`

- 기존 모델 Post에 category 속성을 추가하는 새로운 마이그레이션 생성:

`rails generate migration {{AddCategoryToPost}} {{category:string}}`

- 제목과 본문 속성을 미리 정의하여 Post라는 모델을 위한 스캐폴드 생성:

`rails generate scaffold {{Post}} {{title:string}} {{body:text}}`
