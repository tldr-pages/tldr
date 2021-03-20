# nms

> A cool (piped) text decryption effect.
> More information: <https://github.com/bartobri/no-more-secrets>.

- Decrypt "Hello, World!" after a keystroke:

`echo "Hello, World! | nms"`

- Decrypt the output of `ls -la` automatically:

`ls -la | nms -a`

- Decrypt the content of `secret_message.txt` automatically with red output:

`cat secret_message.txt | nms -a -f red`

- Clear the screen prior to decrypt `git status` automatically:

`git status | nms -a -c`
