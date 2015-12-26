default: lint

all: setup index

index:
	@echo "WARNING!"
	@echo "Index rebuilding is deprecated."
	@echo "You should not do it, unless you understand why you doing this."
	@echo
	@TLDRHOME=`pwd` ./scripts/build_index.rb
	@echo "Index rebuilt."

setup: hooks deps

hooks:
	@cp ./scripts/pre-commit .git/hooks
	@chmod +x .git/hooks/pre-commit
	@echo "Git pre-commit hook installed."

deps:
	@bundle
	@echo "OK"

lint:
	@bundle exec mdl --style ./scripts/markdown-style.rb pages

.PHONY: default index setup hooks deps lint
