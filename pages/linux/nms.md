# nms

> A cool (piped) text decryption effect.
> More information: <https://github.com/bartobri/no-more-secrets>.

- Decrypting "Hello, World!" after a keystroke:

`echo "Hello, World! | nms"`

- Decrypting the output of `ls -la` automatically:

`ls -la | nms -a`

- Decrypting the content of `secret_message.txt` automatically with red output:

`cat secret_message.txt | nms -a -f red`

- Clearing the screen prior to decrypting `git status` automatically:

`git status | nms -a -c`
