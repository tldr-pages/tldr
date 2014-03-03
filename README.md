[![Travis CI](https://api.travis-ci.org/rprieto/tldr.png)](https://travis-ci.org/rprieto/tldr) [![Dependency Status](https://david-dm.org/rprieto/tldr.png?theme=shields.io)](https://david-dm.org/rprieto/tldr) [![devDependency Status](https://david-dm.org/rprieto/tldr/dev-status.png?theme=shields.io)](https://david-dm.org/rprieto/tldr#info=devDependencies)

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

I'm sure people could benefit from simplified "show me the common usages" man pages.
What about:

![tldr screenshot](http://raw.github.com/rprieto/tldr/master/screenshot.png)


# Installing

[![NPM](https://nodei.co/npm/tldr.png)](https://www.npmjs.org/package/tldr)

```bash
$ npm install -g tldr
```

*Note: TLDR is still in early versions. We try to minimise breaking changes, but if you run into issues please try to download the latest package again.*

# Configuration

You can configure the `tldr` client by adding a `.tldrrc` file in your HOME directory. This file has to be valid JSON.

```json
{
  "remote": {
    "url": "http://raw.github.com/rprieto/tldr/master/pages",
    "cache": "30 days"
  },
  "colors": {
    "text": "green",
    "command-background": "black",
    "command-foreground": "red",
    "command-token": "white"
  }
}
```

# Contributing

- Your favourite command isn't covered?
- You can think of more examples?
- New features?

Contribution are most welcome! Have a look [over here](https://github.com/rprieto/tldr/blob/master/CONTRIBUTING.md) for a few rough guidelines.

