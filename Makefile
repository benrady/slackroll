# Modify the path so that we can find Jasmine and other tools
PATH  := node_modules/.bin:$(PATH)

# Normal make targets represet files or directories that need to be built. Phony targets don't.
.PHONY: all clean test dist deps

testdeps = .testdeps
deps = .deps

# The default target
all: clean test

$(deps) :
	mkdir -p $(deps)
	pip install boto3 -t $(deps)

$(testdeps) : $(deps)
	mkdir -p $(testdeps)
	pip install pytest -t $(testdeps)

test: $(testdeps)
	./scripts/test

clean: 
	rm -rf dist
	rm -rf archive.zip

archive.zip: $(deps) clean
	mkdir -p dist
	cp -r $(deps) dist/
	cp -r slackroll dist/
	cd dist; zip -r ../archive.zip * $(deps)
	rm -rf dist

dist: archive.zip

deploy: dist
	@echo "Deploying Lambda Functions"
	./scripts/deploy
