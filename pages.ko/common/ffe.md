# ffe

> 플랫 데이터베이스 파일에서 필드를 추출하고 다른 형식으로 씀.
> 입력을 해석하고 출력 형식을 지정하려면 구성 파일이 필요.
> 더 많은 정보: <https://ff-extractor.sourceforge.net/ffe.html>.

- 지정된 데이터 구성을 사용하여 모든 입력 데이터를 표시:

`ffe --configuration={{경로/대상/구성.ffe}} {{경로/대상/입력}}`

- 입력 파일을 새로운 형식의 출력 파일로 변환:

`ffe --output={{path/to/output}} -c {{경로/대상/구성.ffe}} {{경로/대상/입력}}`

- `~/.fferc` 구성 파일의 정의에서 입력 구조 및 출력 형식을 선택:

`ffe --structure={{structure}} --print={{format}} {{경로/대상/입력}}`

- 선택한 필드만 작성하기:

`ffe --field-list="{{FirstName,LastName,Age}}" -c {{경로/대상/구성.ffe}} {{경로/대상/입력}}`

- 표현식과 일치하는 레코드만 작성:

`ffe -e "{{LastName=Smith}}" -c {{경로/대상/구성.ffe}} {{경로/대상/입력}}`

- 도움말 표시:

`ffe --help`
