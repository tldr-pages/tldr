# jupytext

> Jupyter 노트북을 일반 텍스트 문서로 변환하고, 다시 노트북으로 변환합니다.
> 더 많은 정보: <https://jupytext.readthedocs.io>.

- 노트북을 `.ipynb`/`.py`로 쌍으로 변환:

`jupytext --set-formats ipynb,py {{노트북.ipynb}}`

- 노트북을 `.py` 파일로 변환:

`jupytext --to py {{노트북.ipynb}}`

- `.py` 파일을 출력 없이 노트북으로 변환:

`jupytext --to notebook {{노트북.py}}`

- `.md` 파일을 노트북으로 변환하고 실행:

`jupytext --to notebook --execute {{노트북.md}}`

- 노트북의 입력 셀을 업데이트하고 출력 및 메타데이터를 유지:

`jupytext --update --to notebook {{노트북.py}}`

- 노트북의 모든 쌍으로 연결된 표현 업데이트:

`jupytext --sync {{노트북.ipynb}}`
