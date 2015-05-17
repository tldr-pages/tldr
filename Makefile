all: setup index

index:
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
	@GEM_PATH=.gem find pages -exec .gem/bin/mdl {} --style ./scripts/markdown-style.rb 1>&2 \;
	
lint-changed:
	@./scripts/lint-changed.sh

.PHONY: index setup hooks deps lint lint-changed
