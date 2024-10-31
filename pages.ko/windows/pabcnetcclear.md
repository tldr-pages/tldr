# pabcnetcclear

> PascalABC.NET 소스 파일을 전처리하고 컴파일합니다.
> 더 많은 정보: <https://pascalabc.net>.

- 지정된 소스 파일을 동일한 이름의 실행 파일로 컴파일:

`pabcnetcclear {{경로\대상\소스_파일.pas}}`

- 지정된 소스 파일을 지정된 이름의 실행 파일로 컴파일:

`pabcnetcclear /Output:{{경로\대상\파일.exe}} {{경로\대상\소스_파일.pas}}`

- 디버그 정보를 포함하거나 포함하지 않고 동일한 이름의 실행 파일로 지정된 소스 파일을 컴파일:

`pabcnetcclear /Debug:{{0|1}} {{경로\대상\소스_파일.pas}}`

- 컴파일 중 지정된 경로에서 유닛을 검색하도록 허용:

`pabcnetcclear /SearchDir:{{경로\대상\디렉토리}} {{경로\대상\소스_파일.pas}}`

- 지정된 소스 파일을 실행 파일로 컴파일하고 심볼 정의:

`pabcnetcclear /Define:{{심볼}} {{경로\대상\소스_파일.pas}}`
