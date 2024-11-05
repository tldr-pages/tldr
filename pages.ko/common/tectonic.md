# tectonic

> 현대적이고 독립적인 TeX/LaTeX 엔진.
> 더 많은 정보: <https://tectonic-typesetting.github.io/book/latest>.

- 독립적인 TeX/LaTeX 파일 컴파일:

`tectonic -X compile {{경로/대상/파일.tex}}`

- SyncTeX 데이터를 사용하여 독립적인 TeX/LaTeX 파일 컴파일:

`tectonic -X compile --synctex {{경로/대상/파일.tex}}`

- 현재 디렉토리에 tectonic 프로젝트 초기화:

`tectonic -X init`

- 지정된 디렉토리에 tectonic 프로젝트 초기화:

`tectonic -X new {{프로젝트_이름}}`

- 현재 디렉토리의 프로젝트 빌드:

`tectonic -X build`

- 변경 시 현재 디렉토리의 프로젝트를 빌드하는 감시자 시작:

`tectonic -X watch`
