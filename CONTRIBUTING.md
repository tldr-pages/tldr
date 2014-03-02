# Contributing

- Your favourite command isn't covered?
- You can think of more examples?
- New features?

Contribution are most welcome!

## Contributing content

All `tldr` pages are stored in Markdown right here on Github.
Just open an issue or send a pull request and we'll merge it ASAP.

Note that `tldr` is focussed on concrete examples. Pages should not try to cover all possible examples and combinations of flags. Instead, focus on the 5 or 6 most common usages. When in doubt, keep new command-line users in mind.

For now, the format of each page has to match the following:

```
# command-name

> Short description
> Max 1 or 2 lines

- example description

`command -arg1 -arg2`

- example description

`command -arg1 -arg2`
```

Eventually we might relax the format to accept any Markdown, but for now this has the advantage of adding some consitency between all pages, and making sure we focus on concrete examples rather than lengthy explanation of the different flags.

In the odd case you need a few examples grouped together, the convention so far is:

```
- example description

`command -arg1`
`command -arg2`
```

## Contributing code

We also welcome code contributions! `tldr` is definitely open to new ideas, and have already accepted a lot of new features, new flags, and general bug fixes.

That being said, if it's something sizeable or a brand new feature, it's a good idea to open an issue beforehand to discuss it openly and gather some feedback.

*Quick dev notes:*

```bash
npm test              # run the unit tests
npm start             # start a local server for TLDR pages
npm run example       # try out local fetching/rendering logic
```

---------------------------------------

**Footnote:** tldr is under MIT license. You're free to modify or redistribute the source and content. That being said, but why not contribute over here? :)
