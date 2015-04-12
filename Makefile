setup:
	@cp ./scripts/pre-commit .git/hooks
	@chmod +x .git/hooks/pre-commit
	@echo "Git pre-commit hook installed."

index:
	@scripts/build_index.rb

backticks:
	@scripts/backticks.rb
