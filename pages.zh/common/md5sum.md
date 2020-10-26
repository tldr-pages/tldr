# md5sum

> 计算 MD5 加密校验和.

- 计算文件的 MD5 校验和:

`md5sum {{filename1}}`

- 计算多个文件的 MD5 校验和:

`md5sum {{filename1}} {{filename2}}`

- 读取 MD5SUM 的文件并验证所有文件是否具有匹配的校验和:

`md5sum -c {{filename.md5}}`
