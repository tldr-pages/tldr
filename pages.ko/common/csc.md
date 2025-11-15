# csc

> 마이크로 소프트 사의 C# 컴파일러.
> 더 많은 정보: <https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe>.

- 하나 이상의 C# 파일을 CIL 실행파일로 컴파일:

`csc {{경로/입력파일_a.cs}} {{경로/입력파일_b.cs}}`

- 출력 파일 이름 지정:

`csc /out:{{경로/파일명}} {{경로/입력파일.cs}}`

- 실행 파일 대신 '.dll' 라이브러리로 컴파일:

`csc /target:library {{경로/입력파일.cs}}`

- 다른 어셈블리 참조:

`csc /reference:{{경로/라이브러리.dll}} {{경로/입력파일.cs}}`

- 리소스 포함:

`csc /resource:{{경로/리소스파일}} {{경로/입력파일.cs}}`

- XML 문서 자동 생성:

`csc /doc:{{경로/출력파일.xml}} {{경로/입력파일.cs}}`

- 아이콘 지정:

`csc /win32icon:{{경로/아이콘.ico}} {{경로/입력파일.cs}}`

- 키 파일을 사용하여 결과 어셈블리의 이름 지정:

`csc /keyfile:{{경로/키파일}} {{경로/입력파일.cs}}`
