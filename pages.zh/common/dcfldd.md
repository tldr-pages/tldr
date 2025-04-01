# dcfldd

> 用于取证和安全的 dd 增强版。
> 更多信息：<https://dcfldd.sourceforge.net/>.

- 将磁盘复制到原始映像文件，并使用 SHA256 对映像进行哈希：

`dcfldd if={{/dev/disk_device}} of={{file.img}} hash=sha256 hashlog={{file.hash}}`

- 将磁盘复制到原始映像文件，并对每个 1 GB 的块进行哈希：

`dcfldd if={{/dev/disk_device}} of={{file.img}} hash={{sha512|sha384|sha256|sha1|md5}} hashlog={{file.hash}} hashwindow={{1G}}`
