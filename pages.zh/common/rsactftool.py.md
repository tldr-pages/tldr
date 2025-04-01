# RsaCtfTool

> 用于 CTF 挑战的 RSA 攻击工具 - 从弱公钥中恢复私钥和/或解密数据。
> 更多信息：<https://github.com/RsaCtfTool/RsaCtfTool>.

- 从公钥文件中恢复私钥：

`RsaCtfTool.py --publickey {{path/to/key.pub}} --private`

- 使用公钥解密文件：

`RsaCtfTool.py --publickey {{path/to/key.pub}} --decryptfile {{path/to/ciphered_file}}`

- 解密特定的密文字符串：

`RsaCtfTool.py --publickey {{path/to/key.pub}} --decrypt "{{ciphertext}}"`

- 从密钥文件中转储 RSA 密钥组件（例如，模数、指数）：

`RsaCtfTool.py --dumpkey --key {{path/to/key.pub}}`

- 运行特定攻击（例如，费马分解）以恢复私钥：

`RsaCtfTool.py --publickey {{path/to/key.pub}} --private --attack fermat`

- 从模数 (n) 和指数 (e) 生成公钥：

`RsaCtfTool.py --createpub -n {{modulus}} -e {{exponent}}`

- 尝试所有可用攻击以恢复私钥：

`RsaCtfTool.py --publickey {{path/to/key.pub}} --private --attack all`