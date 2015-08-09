# What is this?

New to the command-line world? Or just a little rusty?
Or, like me, you can't always remember the arguments to `lsof` or `tar`?

Maybe it doesn't help that the first option explained in `man tar` is:

```
-b blocksize
   Specify the block size, in 512-byte records, for tape drive I/O.
   As a rule, this argument is only needed when reading from or writing to tape drives,
   and usually not even then as the default block size of 20 records (10240 bytes) is very common.
```

I'm sure people could benefit from simplified "show me the common usages" man pages. What about:

![tldr screenshot](http://raw.github.com/rprieto/tldr/master/screenshot.png)

This repository is just that: an ever-growing collection of examples for the most common UNIX / Linux / OSX / SunOS commands.

## Clients

You can access these pages on your computer using one of the following clients:

- [Node.js client](https://github.com/rprieto/tldr-node-client) : `npm install -g tldr`
- [Python client](https://github.com/felixonmars/tldr-python-client) : `pip install tldr`
- [Go client](https://github.com/pranavraja/tldr) : `go get github.com/pranavraja/tldr` or [platform binaries](https://github.com/pranavraja/tldr/releases)
- [Exilir client](https://github.com/edgurgel/tldr): binaries available soon
- [C++ client](https://github.com/tldr-pages/tldr-cpp-client): `brew tap tldr-pages/tldr && brew install tldr`
- [Android client](https://github.com/gianasista/tldr-viewer): available on [Google Play](https://play.google.com/store/apps/details?id=de.gianasista.tldr_viewer)
- [Ruby client](https://github.com/YellowApple/tldrb): `gem install tldrb`
- [Web client](https://github.com/ostera/tldr.js): try tldr on your browser [here](https://ostera.github.io/tldr.js)!

Let us know if you are building one and we can add it to this list!

## Contributing

- Your favourite command isn't covered?
- You can think of more examples?

Contribution are most welcome! Have a look [over here](https://github.com/rprieto/tldr/blob/master/CONTRIBUTING.md) for some rough guidelines.
