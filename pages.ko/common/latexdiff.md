# latexdiff

> 두 개의 LaTeX 파일 간의 차이점을 확인.
> 더 많은 정보: <https://ctan.org/pkg/latexdiff>.

- 서로 다른 버전의 LaTeX 파일 간의 변경 사항 확인 (결과 LaTeX 파일은 밑줄로 차이점을 표시하도록 컴파일 가능):

`latexdiff {{오래된.tex}} {{새.tex}} > {{차이.tex}}`

- 서로 다른 버전의 LaTeX 파일 간의 변경 사항을 굵은 글씨로 강조하여 확인:

`latexdiff --type=BOLD {{오래된.tex}} {{새.tex}} > {{차이.tex}}`

- 서로 다른 버전의 LaTeX 파일 간의 변경 사항을 확인하고, 방정식의 작은 변경 사항을 추가 및 삭제된 그래픽과 함께 표시:

`latexdiff --math-markup=fine --graphics-markup=both {{오래된.tex}} {{새.tex}} > {{차이.tex}}`
