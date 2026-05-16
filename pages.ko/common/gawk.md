# gawk

> 파일 작업을 위한 범용 프로그래밍 언어인 GNU 버전의 awk.
> 관련 항목: `awk`.
> 더 많은 정보: <https://www.gnu.org/software/gawk/manual/gawk.html>.

- 공백으로 구분된 파일의 5번째 열(field) 출력:

`gawk '{print $5}' {{경로/대상/파일}}`

- 공백으로 구분된 파일에서 "foo"를 포함한 줄의 2번쨰 열 출력:

`gawk '/{{foo}}/ {print $2}' {{경로/대상/파일}}`

- 쉼표를(공백 대신) 필드 구분자로 사용하여, 각 줄의 마지막 열을 출력:

`gawk {{[-F|--field-separator]}} ',' '{print $NF}' {{경로/대상/파일}}`

- 파일의 첫 번째 열 값을 모두 합산하여 총합을 출력:

`gawk '{s+=$1} END {print s}' {{경로/대상/파일}}`

- 첫 번째 줄부터 시작하여 매 3번째 줄 출력:

`gawk 'NR%3==1' {{경로/대상/파일}}`

- 조건에 따라 서로 다른 값을 출력:

`gawk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' {{경로/대상/파일}}`

- 10번째 열 값이 최소값과 최대값 사이인 모든 줄 출력:

`gawk '($10 >= {{최소값}} && $10 <= {{최대값}})' {{경로/대상/파일}}`

- UID >=1000인 사용자 테이블을 헤더 포함한 포맷된 출력 형식으로 표시(:을 구분자로 사용), (`%-20s`은 문자열을 왼쪽 정렬해 최소 20칸으로 출력, `%6s`은 문자열을 오른쪽 정렬해 최소 6카능로 출력한다는 의미):

`gawk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
