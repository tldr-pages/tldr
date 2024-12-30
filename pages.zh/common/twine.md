# twine

> 在 PyPI 上发布 Python 包的工具。
> 更多信息：<https://twine.readthedocs.io/en/stable/#commands>。

- 上传到 PyPI：

`twine upload dist/*`

- 上传到测试 PyPI [r]epository 以验证内容是否正确：

`twine upload -r testpypi dist/*`

- 使用指定的 [u]sername 和 [p]assword 上传到 PyPI：

`twine upload -u {{username}} -p {{password}} dist/*`

- 上传到替代的存储库 URL：

`twine upload --repository-url {{repository_url}} dist/*`

- 检查你的分发的长描述是否能够在 PyPI 上正确渲染：

`twine check dist/*`

- 使用特定的 pypirc 配置文件上传：

`twine upload --config-file {{configuration_file}} dist/*`

- 如果某个文件已经存在，继续上传文件（仅在上传到 PyPI 时有效）：

`twine upload --skip-existing dist/*`

- 上传到 PyPI，并显示详细信息：

`twine upload --verbose dist/*`