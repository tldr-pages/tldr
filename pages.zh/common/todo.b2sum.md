# b2sum

> BLAKE2总和检验码加密算法
> 详见: <https://blake2.net/#su>.

- 计算出一个文件的 BLAKE2 检验和:

`b2sum {{filename1}}`

- 计算出多个文件的 BLAKE2 检验和:

`b2sum {{filename1}} {{filename2}}`

- Read a file of BLAKE2 sums and filenames and verify all files have matching checksums:

`b2sum -c {{filename.b2}}`

- Calculate the BLAKE2 checksum from `stdin`:

`{{somecommand}} | b2sum`
