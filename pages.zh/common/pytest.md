# pytest

> 运行 Python 测试。
> 更多信息：<https://docs.pytest.org/>.

- 运行指定文件中的测试：

`pytest {{path/to/test_file1.py path/to/test_file2.py ...}}`

- 运行名称匹配特定 [k]eyword 表达式的测试：

`pytest -k {{expression}}`

- 一旦测试失败或遇到错误即退出：

`pytest --exitfirst`

- 运行匹配或排除标记的测试：

`pytest -m {{marker_name1 and not marker_name2}}`

- 运行测试直到失败，从上次失败的测试继续：

`pytest --stepwise`

- 运行测试时不捕获输出：

`pytest --capture=no`
