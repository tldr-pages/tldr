# hledger import

> Import new transactions from one or more data files to the main journal.
> More information: <https://hledger.org/hledger.html#import>.

- Import new transactions from `bank.csv`, using `bank.csv.rules` to convert:

`hledger import {{path/to/bank.csv}}`

- Show what would be imported from these two files, without doing anything:

`hledger import {{path/to/bank1.csv}} {{path/to/bank2.csv}} --dry-run`

- Import new transactions from all CSV files, using the same rules for all:

`hledger import --rules-file {{common.rules}} *.csv`

- Show conversion errors or results while editing `bank.csv.rules`:

`watchexec -- hledger -f {{path/to/bank.csv}} print`

- Mark `bank.csv`'s current data as seen, as if already imported:

`hledger import --catchup {{path/to/bank.csv}}`

- Mark `bank.csv` as all new, as if not yet imported:

`rm -f .latest.bank.csv`
