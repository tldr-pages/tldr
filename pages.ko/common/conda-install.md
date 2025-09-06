# conda install

> 기존 conda 환경에 패키지를 설치.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/install.html>.

- 현재 활성 conda 환경에 하나 이상의 패키지를 설치:

`conda install {{패키지1 패키지2 ...}}`

- 채널 conda-forge를 사용하여 현재 활성 conda 환경에 단일 패키지를 설치:

`conda install -c conda-forge {{패키지}}`

- conda-forge 채널을 사용하고 다른 채널을 무시하고 현재 활성 conda 환경에 단일 패키지를 설치:

`conda install -c conda-forge --override-channels {{패키지}}`

- 특정 버전의 패키지를 설치:

`conda install {{패키지}}={{버전}}`

- 특정 환경에 패키지를 설치:

`conda install --name {{환경}} {{패키지}}`

- 현재 환경에서 패키지 업데이트:

`conda install --upgrade {{패키지}}`

- 메시지를 표시하지 않고 동의하여 패키지를 설치:

`conda install --yes {{패키지}}`
