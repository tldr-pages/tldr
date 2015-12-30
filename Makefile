default: lint

index:
	@echo "WARNING!"
	@echo "Index rebuilding is deprecated."
	@echo "You should not do it, unless you understand why you doing this."
	@echo
	@TLDRHOME=`pwd` ./scripts/build_index.rb
	@echo "Index rebuilt."

setup: prerequisites hooks deps

prerequisites:
	@echo
	@echo "IMPORTANT!"
	@echo "Before setting up hooks, make sure you have read Contributing Guidelines"
	@echo "https://github.com/tldr-pages/tldr/blob/master/CONTRIBUTING.md#submitting-a-pull-request"
	@echo
	@echo "TL;DR:"
	@echo "1. Install Ruby suitable for your system"
	@echo "2. Run 'gem install bundler'"
	@echo

hooks:
	@cp ./scripts/pre-commit .git/hooks
	@chmod +x .git/hooks/pre-commit
	@echo "Git pre-commit hook installed."

deps:
	@bundle
	@echo "OK"

lint:
	@bundle exec mdl --style ./scripts/markdown-style.rb pages

.PHONY: default index setup prerequisites hooks deps lint
