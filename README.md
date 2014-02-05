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

```bash
$ npm install -g tldr
```

# Contributing

Your favourite command isn't covered? You can think of more examples? New features?

`tldr` is under [MIT license](http://opensource.org/licenses/MIT). You're free to modify or redistribute the source and content, but why not contribute over here? :)

Just [open an issue](http://github.com/rprieto/tldr/issues) or [send a pull request](https://github.com/rprieto/tldr/pulls), it's all **Markdown** stored right here on Github.

The rough guidelines are:

- each command's description should be short and sweet
- give around 5 examples of the most common usages
- when in doubt, keep new command-line users in mind

# Dev notes

- To run the tests:

```
npm test
```

- To try out new fetching/rendering logic locally

```
npm start
npm run example
```


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/rprieto/tldr/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

