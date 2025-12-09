# sphinx-build

> Sphinx 문서 생성기.
> 더 많은 정보: <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>.

- 문서 빌드:

`sphinx-build -b {{html|epub|text|latex|man|...}} {{경로/대상/소스_폴더}} {{경로/대상/빌드_폴더}}`

- readthedocs.io를 위한 문서 빌드 (sphinx-rtd-theme pip 패키지가 필요):

`sphinx-build -b {{html}} {{경로/대상/문서_폴더}} {{경로/대상/빌드_폴더}}`
