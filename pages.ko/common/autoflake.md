# autoflake

> Python 코드에서 사용하지 않는 가져오기 및 변수를 제거하는 도구.
> 더 많은 정보: <https://github.com/myint/autoflake>.

- 단일 파일에서 사용되지 않는 변수를 제거하고 차이점을 표시:

`autoflake --remove-unused-variables {{경로/대상/파일.py}}`

- 여러 파일에서 사용되지 않은 가져오기를 제거하고 차이점을 표시:

`autoflake --remove-all-unused-imports {{경로/대상/파일1.py 경로/대상/파일2.py ...}}`

- 파일에서 사용되지 않는 변수를 제거하고 파일을 덮어씀:

`autoflake --remove-unused-variables --in-place {{경로/대상/파일.py}}`

- 디렉터리의 모든 파일에서 사용되지 않는 변수를 반복적으로 제거하여 각 파일을 덮어씀:

`autoflake --remove-unused-variables --in-place --recursive {{경로/대상/디렉터리}}`
