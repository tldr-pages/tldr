index:
	@TLDRHOME=`pwd` ./scripts/build_index.rb
	@echo "Index rebuilt."

setup:
	@cp ./scripts/pre-commit .git/hooks
	@chmod +x .git/hooks/pre-commit
	@echo "Git pre-commit hook installed."
	
	@gem install mdl --install-dir .gem --no-rdoc --no-ri
	@echo "Installed required Ruby gems under .gem"
	
lint: 
	@GEM_PATH=.gem find pages -exec .gem/bin/mdl {} --style ./scripts/markdown-style.rb 1>&2 \;
	
lint-changed:
	@./scripts/lint-changed.sh
	
