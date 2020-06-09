# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

certs:
	./generate-certs.sh

build: certs  ## build all images
	docker-compose build

up:  ## bring eventstore up
	docker-compose up -d eventstore

test:  ## run tests
	docker-compose run --rm --no-deps tests

clean:  ## take down containers
	docker-compose down
	rm -rf certs

all: clean build up test
