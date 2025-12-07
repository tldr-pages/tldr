# numfmt

> Convert numbers to and from human-readable strings.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/numfmt-invocation.html>.

- Convert 1.5K (SI Units) to 1500:

`numfmt --from si 1.5K`

- Convert 1500 to 1.5K (SI Units):

`numfmt --to si 1500`

- Convert 1.5K (IEC Units) to 1536:

`numfmt --from iec 1.5K`

- Use appropriate conversion based on the suffix

`numfmt --from auto {{1.5Ki}}`

- Convert 5th field (1-indexed) to IEC Units without converting header:

`ls -l | numfmt --header=1 --field 5 --to iec`

- Convert to IEC units, pad with 5 characters, left aligned:

`du {{[-s|--summarize]}} * | numfmt --to iec --format "%-5f"`
