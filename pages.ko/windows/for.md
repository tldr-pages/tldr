# for

> 조건에 따라 명령을 여러 번 실행.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/for>.

- 지정된 집합에 대해 명령 실행:

`for %{{변수}} in ({{항목_a 항목_b 항목_c}}) do ({{echo 루프가 실행됩니다}})`

- 주어진 숫자 범위를 반복:

`for /l %{{변수}} in ({{시작}}, {{단계}}, {{끝}}) do ({{echo 루프가 실행됩니다}})`

- 주어진 파일 목록을 반복:

`for %{{변수}} in ({{경로\대상\파일1.ext 경로\대상\파일2.ext ...}}) do ({{echo 루프가 실행됩니다}})`

- 주어진 디렉토리 목록을 반복:

`for /d %{{변수}} in ({{경로\대상\폴더1.ext 경로\대상\폴더2.ext ...}}) do ({{echo 루프가 실행됩니다}})`

- 모든 디렉토리에서 지정된 명령 수행:

`for /d %{{변수}} in (*) do (if exist %{{변수}} {{echo 루프가 실행됩니다}})`
