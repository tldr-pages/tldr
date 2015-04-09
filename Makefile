index:
	@TLDRHOME=`pwd` ./scripts/build_index.rb
	@echo "Index rebuilt."

setup:
	@cp ./scripts/pre-commit .git/hooks
	@chmod +x .git/hooks/pre-commit
	@echo "Git pre-commit hook installed."
