# rename

> 정규 표현식을 사용하여 파일 또는 파일 그룹의 이름을 변경.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/rename.2.html>.

- 지정된 파일들의 파일명에서 `from`을 `to`로 변경:

`rename 's/{{from}}/{{to}}/' {{*.txt}}`
