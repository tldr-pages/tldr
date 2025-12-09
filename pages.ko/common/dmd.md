# dmd

> 공식적 D 컴파일러.
> 더 많은 정보: <https://dlang.org/dmd.html>.

- D 소스 파일 빌드:

`dmd {{경로/대상/소스.d}}`

- 모든 템플릿 인스턴스화에 대한 코드 생성:

`dmd -allinst`

- 제어 범위 확인:

`dmd -boundscheck={{on|safeonly|off}}`

- 사용 가능한 모든 체크사항에 대한 나열:

`dmd -check={{h|help|?}}`

- 색깔있는 콘솔 출력을 보여줌:

`dmd -color`
