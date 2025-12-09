# rake

> Ruby용 Make와 유사한 프로그램.
> `rake`의 작업은 Rakefile에 지정됩니다.
> 더 많은 정보: <https://ruby.github.io/rake>.

- `default` Rakefile 작업 실행:

`rake`

- 특정 작업 실행:

`rake {{작업}}`

- 동시에 `n`개의 작업 병렬 실행 (기본값은 CPU 코어 수 + 4):

`rake --jobs {{n}}`

- 특정 Rakefile 사용:

`rake --rakefile {{경로/대상/Rakefile}}`

- 다른 디렉토리에서 `rake` 실행:

`rake --directory {{경로/대상/폴더}}`
