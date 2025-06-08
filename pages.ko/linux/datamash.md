# datamash

> 입력 텍스트 데이터 파일에 대해 기본적인 수치, 텍스트 및 통계 작업 수행.
> 더 많은 정보: <https://www.gnu.org/software/datamash/manual/html_node/Invoking-datamash.html>.

- 한 열의 숫자에 대한 최대값, 최소값, 평균 및 중앙값 계산:

`seq 3 | datamash max 1 min 1 mean 1 median 1`

- 부동 소수점 숫자(소수점은 ","로 표시)를 포함한 한 열의 평균 계산:

`echo -e '1.0\n2.5\n3.1\n4.3\n5.6\n5.7' | tr '.' ',' | datamash mean 1`

- 지정된 소수 자릿수로 한 열의 숫자 평균 계산:

`echo -e '1\n2\n3\n4\n5\n5' | datamash {{[-R|--round]}} {{원하는_소수_자릿수}} mean 1`

- "Na"와 "NaN"(문자열)을 무시하고 한 열의 숫자 평균 계산:

`echo -e '1\n2\nNa\n3\nNaN' | datamash --narm mean 1`
