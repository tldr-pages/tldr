# cmp

> 두 개의 파일 비교.
> 더 많은 정보: <https://www.gnu.org/software/diffutils/manual/diffutils.html#Invoking-cmp>.

- 파일 간의 첫 번째 바이트 번호와 선 번호의 차이를 찾습니다:

`cmp {{파일1}} {{파일2}}`

- 모든 바이트 수와 다른 바이트의 차이 찾기:

`cmp {{[-l|--verbose]}} {{파일1}} {{파일2}}`
