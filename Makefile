# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build:  ## build all images
	docker-compose build


up:  ## bring containers up in the background
	docker-compose up -d

server_ca.pem:
	docker-compose run --entrypoint=cat eventstore /opt/eventstore/dev-ca/ca.pem > server_ca.pem

server_cert.pem:
	docker-compose run --entrypoint=cat eventstore /opt/eventstore/dev-ca/server1.pem > server_cert.pem

test: server_ca.pem server_cert.pem
	docker-compose run --rm --no-deps tests

clean:
	docker-compose down
