# nth

> Name That Hash - 立即识别任意哈希的类型。
> 更多信息：<https://github.com/hashpals/name-that-hash>.

- 识别一个哈希：

`nth -t {{5f4dcc3b5aa765d61d8327deb882cf99}}`

- 识别文件中的哈希：

`nth -f {{path/to/hashes}}`

- 以 JSON 格式输出：

`nth -t {{5f4dcc3b5aa765d61d8327deb882cf99}} -g`

- 在识别前先将哈希从 Base64 解码：

`nth -t {{NWY0ZGNjM2I1YWE3NjVkNjFkODMyN2RlYjg4MmNmOTkK}} -b64`