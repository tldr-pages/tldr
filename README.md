# tldr

[![Build Status][travis-image]][travis-url]
[![Gitter chat][gitter-image]][gitter-url]
[travis-url]: https://travis-ci.org/tldr-pages/tldr
[travis-image]: https://img.shields.io/travis/tldr-pages/tldr.svg
[gitter-url]: https://gitter.im/tldr-pages/tldr
[gitter-image]: https://img.shields.io/gitter/room/tldr-pages/tldr.svg

*tldr* is a collection of simplified and community-driven man pages.

## What does tldr mean?
TL;DR stands for "Too Long; Didn't Read".
It originates in Internet slang, where it is used to indicate parts of the text skipped as too lengthy.
Read more in the [TLDR article on Wikipedia](https://en.wikipedia.org/wiki/TL;DR).

## What is tldr?

New to the command-line world? Or just a little rusty?
Or perhaps you can't always remember the arguments to `lsof`, or `tar`?

Maybe it doesn't help that the first option explained in `man tar` is:

```
-b blocksize
   Specify the block size, in 512-byte records, for tape drive I/O.
   As a rule, this argument is only needed when reading from or writing to tape drives,
   and usually not even then as the default block size of 20 records (10240 bytes) is very common.
```

Surely people could benefit from simplified "show me the common usages" man pages. What about:

![tldr screenshot](http://raw.github.com/tldr-pages/tldr/master/screenshot.png)

This repository is just that:
an ever-growing collection of examples
for the most common UNIX / Linux / OSX / SunOS commands.

## Clients

You can access these pages on your computer using one of the following clients:

- [Node.js client](https://github.com/tldr-pages/tldr-node-client) : `npm install -g tldr`
- [Python client](https://github.com/tldr-pages/tldr-python-client) : `pip install tldr`
- [Python client](https://github.com/lord63/tldr.py): `pip install tldr.py`
- [Go client](https://github.com/pranavraja/tldr): `go get github.com/pranavraja/tldr`
  or [platform binaries](https://github.com/pranavraja/tldr/releases)
- [Elixir client](https://github.com/tldr-pages/tldr_elixir_client): binaries available soon
- [C++ client](https://github.com/tldr-pages/tldr-cpp-client): `brew tap tldr-pages/tldr && brew install tldr`
- Android client:
  - [tldr-viewer](https://github.com/gianasista/tldr-viewer), available on
    [Google Play](https://play.google.com/store/apps/details?id=de.gianasista.tldr_viewer)
  - [tldroid](https://github.com/hidroh/tldroid), available on
    [Google Play](https://play.google.com/store/apps/details?id=io.github.hidroh.tldroid)
- [Ruby client](https://github.com/YellowApple/tldrb): `gem install tldrb`
- [R client](https://github.com/kirillseva/tldrrr): `devtools::install_github('kirillseva/tldrrr')`
- [Web client](https://github.com/ostera/tldr.jsx): try tldr on your browser
  [here](https://ostera.github.io/tldr.jsx)!

Let us know if you are building one and we can add it to this list!

## Contributing

- Your favourite command isn't covered?
- You can think of more examples for an existing command?

Contributions are most welcome!
Have a look at the [contributing guidelines](https://github.com/tldr-pages/tldr/blob/master/CONTRIBUTING.md)
and go ahead!
