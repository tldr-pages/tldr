# twine

> Python 패키지를 PyPI에 배포하는 도구.
> 더 많은 정보: <https://twine.readthedocs.io/en/stable/#commands>.

- PyPI에 업로드:

`twine upload dist/*`

- Test PyPI 저장소에 업로드하여 검증:

`twine upload -r testpypi dist/*`

- 지정된 사용자 이름과 비밀번호로 PyPI에 업로드:

`twine upload -u {{사용자명}} -p {{비밀번호}} dist/*`

- 대체 저장소 URL로 업로드:

`twine upload --repository-url {{저장소_URL}} dist/*`

- 배포의 긴 설명이 PyPI에서 올바르게 렌더링되는지 확인:

`twine check dist/*`

- 특정 pypirc 설정 파일을 사용하여 업로드:

`twine upload --config-file {{설정_파일}} dist/*`

- 파일이 이미 존재할 경우 업로드 계속 (PyPI에 업로드할 때만 유효):

`twine upload --skip-existing dist/*`

- 자세한 정보를 표시하며 PyPI에 업로드:

`twine upload --verbose dist/*`
