# faker

> 가짜 데이터를 생성하기 위한 Python 라이브러리 및 CLI 도구.
> 더 많은 정보: <https://faker.readthedocs.io/en/master/>.

- 모든 가짜 데이터 제공자와 예시를 출력:

`faker`

- 특정 타입의 가짜 데이터 생성:

`faker {{name|address|passport_full|credit_card_full|phone_number|email|company|date_time|user_name|password|job|...}}`

- 특정 국가의 로케일로 여러 개 주소 생성 (`localectl list-locales | cut --delimiter . --fields 1`로 로케일 확인):

`faker {{[-r|--repeat]}} {{숫자}} {{[-l|--lang]}} {{de_DE|de_CH|...}} address`

- 특정 국가의 도시 이름 여러 개 생성 후 파일로 저장 (`localectl list-locales | cut --delimiter . --fields 1` 로 로케일 확인):

`faker {{[-r|--repeat]}} {{숫자}} {{[-l|--lang]}} {{en_AU|en_US|...}} city -o {{경로/대상/파일.txt}}`

- 상세 출력을 포함해 랜덤 HTTP user-agent 여러 개 생성:

`faker {{[-r|--repeat]}} {{숫자}} {{[-v|--verbose]}} user_agent`

- 특정 구분자를 사용해 여러 개의 도메인 이름 생성:

`faker {{[-r|--repeat]}} {{숫자}} {{[-s|--sep]}} '{{,}}' domain_name`
