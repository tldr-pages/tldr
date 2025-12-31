# jupyter

> 코드, 시각화 및 노트를 포함한 문서를 생성하고 공유할 수 있는 웹 애플리케이션.
> 주로 데이터 분석, 과학 컴퓨팅 및 머신 러닝에 사용됩니다.
> 더 많은 정보: <https://docs.jupyter.org/en/latest/>.

- 현재 디렉토리에서 Jupyter 노트북 서버 시작:

`jupyter notebook`

- 특정 Jupyter 노트북 열기:

`jupyter notebook {{예제.ipynb}}`

- 특정 Jupyter 노트북을 다른 형식으로 내보내기:

`jupyter nbconvert --to {{html|markdown|pdf|script}} {{예제.ipynb}}`

- 특정 포트에서 서버 시작:

`jupyter notebook --port {{포트}}`

- 현재 실행 중인 노트북 서버 나열:

`jupyter notebook list`

- 현재 실행 중인 서버 중지:

`jupyter notebook stop`

- 설치되어 있다면 현재 디렉토리에서 JupyterLab 시작:

`jupyter lab`
