# Modify the path so that we can find Jasmine and other tools
PATH  := node_modules/.bin:$(PATH)

# Normal make targets represet files or directories that need to be built. Phony targets don't.
.PHONY: all clean test dist deps

testdeps = .testdeps
env = .env

# The default target
all: clean test

# This needs to be smarter. It doesn't install if the directory exists
# Maybe create a setup.py?
deps: $(env)
	mkdir -p $(deps)
	pip install boto3
	pip install diceroll

testdeps : deps
	pip install pytest

test: testdeps
	./scripts/test

clean: 
	rm -rf dist
	rm -rf archive.zip

archive.zip: deps clean
	mkdir -p dist
	cp -r $(deps) dist/
	cp -r slackroll dist/
	cd dist; zip -r ../archive.zip *
	rm -rf dist

dist: archive.zip

deploy: dist
	@echo "Deploying Lambda Functions"
	./scripts/deploy
