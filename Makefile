.PHONY: index backticks lint setup

index:
	@TLDRHOME=`pwd` ./scripts/build_index.rb
	@echo "Index rebuilt."

backticks:
	@chmod +x scripts/backticks.rb
	@TLDRHOME=`pwd` ./scripts/backticks.rb

lint: backticks

setup:
	@cp ./scripts/pre-commit .git/hooks
	@chmod +x .git/hooks/pre-commit
	@echo "Git pre-commit hook installed."
