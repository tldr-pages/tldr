# funzip

> 추출 없이 아키이브의 첫 번째 (디렉토리가 아닌) 멤버의 내용을 출력.
> 더 많은 정보: <https://manned.org/funzip>.

- Zip 아카이브의 첫 번째 멤버 내용을 출력:

`funzip {{경로/대상/아카이브.zip}}`

- gzip 아카이브의 콘텐츠를 출력:

`funzip {{경로/대상/아카이브.gz}}`

- Zip 또는 gzip 아카이브를 해독하고 콘텐츠를 출력:

`funzip -password {{비밀번호}} {{경로/대상/아카이브}}`
