# hledger print

> Show full journal entries, representing transactions.
> More information: <https://hledger.org/hledger.html#print>.

- Show all transactions in the default journal file:

`hledger print`

- Show transactions, with any implied amounts or costs made explicit:

`hledger print --explicit --infer-costs`

- Show transactions from two specified files, with amounts converted to cost:

`hledger print --file {{path/to/2023.journal}} --file {{path/to/2024.journal}} --cost`

- Show `$` transactions in `*food*` but not `*groceries*` accounts this month:

`hledger print cur:\\$ food not:groceries date:thismonth`

- Show transactions of amount 50 or more, with `whole foods` in their description:

`hledger print amt:'>50' desc:'whole foods'`

- Show cleared transactions, with `EUR` amounts rounded and with decimal commas:

`hledger print --cleared --commodity '1000, EUR' --round hard`

- Write transactions from `foo.journal` as a CSV file:

`hledger print --file {{path/to/foo.journal}} --output-file {{path/to/output_file.csv}}`
