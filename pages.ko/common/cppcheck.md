# cppcheck

> C/C++ 코드를 위한 정적 분석 도구.
> 구문 오류 대신 컴파일러가 일반적으로 감지하지 못하는 버그 유형에 중점을 둠.
> 더 많은 정보: <https://cppcheck.sourceforge.net>.

- 화면에 진행률을 표시하고 오류 메시지를 파일에 로깅하여 현재 디렉토리를 반복적으로 확인:

`cppcheck . 2> cppcheck.log`

- 주어진 디렉토리를 재귀적으로 확인하고, 진행 메시지를 출력하지 않음:

`cppcheck --quiet {{디렉토리/의/경로}}`

- 수행 할 테스트를 지정하여 주어진 파일을 확인(기본적으로 오류만 표시됨):

`cppcheck --enable {{error|warning|style|performance|portability|information|all}} {{file.cpp/의/경로}}`

- 사용 가능한 테스트 목록:

`cppcheck --errorlist`

- 특정 테스트를 무시하고 주어진 파일을 확인:

`cppcheck --suppress {{test_id1}} --suppress {{test_id2}} {{file.cpp/의/경로}}`

- 현재 디렉토리를 확인하여 외부에 있는 include 파일의 경로를 제공(예 : 외부 라이브러리):

`cppcheck -I {{include/디렉토리_1}} -I {{include/디렉토리_2}} .`

- Microsoft Visual Studio 프로젝트 (`*.vcxproj`) 또는 솔루션 (`*.sln`)을 확인:

`cppcheck --project {{project.sln/의/경로}}`
