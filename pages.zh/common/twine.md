# twine

> 用于在 PyPI 上发布 Python 包的工具。
> 更多信息：<https://twine.readthedocs.io/en/stable/#commands>.

- 上传到 PyPI:

`twine upload dist/*`

- 上传到测试 PyPI 仓库以验证显示是否正确:

`twine upload {{[-r|--repository]}} testpypi dist/*`

- 使用指定的用户名和密码上传到 PyPI:

`twine upload {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} dist/*`

- 上传到备用仓库 URL:

`twine upload --repository-url {{repository_url}} dist/*`

- 检查你的分发包的长描述在 PyPI 上是否能正确显示:

`twine check dist/*`

- 使用特定的 pypirc 配置文件上传:

`twine upload --config-file {{configuration_file}} dist/*`

- 如果文件已存在则跳过上传（仅在上传到 PyPI 时有效）:

`twine upload --skip-existing dist/*`

- 上传到 PyPI 并显示详细信息:

`twine upload --verbose dist/*`
