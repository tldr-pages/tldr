index:
	ls -d1 ./pages/**/* | grep .md | awk -F"." '{print $$2}' | awk -F"/" '{print $$4,$$3}' | sort > pages/index.md
	@echo "Index rebuilt."
