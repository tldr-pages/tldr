# pytest

> Python 테스트 실행.
> 더 많은 정보: <https://docs.pytest.org/en/latest/how-to/usage.html>.

- 특정 파일에서 테스트 실행:

`pytest {{경로/대상/테스트_파일1.py 경로/대상/테스트_파일2.py ...}}`

- 특정 [k]eyword 표현식과 일치하는 테스트 실행:

`pytest -k {{표현식}}`

- 테스트가 실패하거나 오류가 발생하면 즉시 종료:

`pytest --exitfirst`

- 마커와 일치하거나 제외하는 테스트 실행:

`pytest -m {{마커_이름1 and not 마커_이름2}}`

- 마지막 실패 테스트부터 계속해서 테스트 실패까지 실행:

`pytest --stepwise`

- 출력을 캡처하지 않고 테스트 실행:

`pytest --capture=no`
