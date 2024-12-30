# in-toto-run

> 在执行供应链步骤时生成链接元数据。
> 更多信息：<https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-run.html>。

- 标记一个 Git 仓库并签署生成的链接文件：

`in-toto-run -n {{tag}} --products {{.}} -k {{key_file}} -- {{git tag v1.0}}`

- 创建一个 tar 包，将文件存储为材料，tar 包作为产品：

`in-toto-run -n {{package}} -m {{project}} -p {{project.tar.gz}} -- {{tar czf project.tar.gz project}}`

- 为审查工作生成签名证明：

`in-toto-run -n {{review}} -k {{key_file}} -m {{document.pdf}} -x`

- 使用 Trivy 扫描镜像并生成链接文件：

`in-toto-run -n {{scan}} -k {{key_file}} -p {{report.json}} -- {{/bin/sh -c "trivy -o report.json -f json <IMAGE>"}}`