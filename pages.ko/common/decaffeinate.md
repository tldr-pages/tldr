# decaffeinate

> CoffeeScript 소스를 최신 JavaScript로 이동.
> 더 많은 정보: <https://decaffeinate-project.org>.

- CoffeeScript 파일을 JavaScript로 변환:

`decaffeinate {{경로/대상/파일.coffee}}`

- CoffeeScript v2 파일을 JavaScript로 변환:

`decaffeinate --use-cs2 {{경로/대상/파일.coffee}}`

- 가져오기 및 내보내기를 위해 require 및 `module.exports`를 변환:

`decaffeinate --use-js-modules {{경로/대상/파일.coffee}}`

- 이름있는 내보내기를 허용하는 CoffeeScript를 변환:

`decaffeinate --loose-js-modules {{경로/대상/파일.coffee}}`
