#!/usr/bin/make

build: # build all containers
	@docker build -t jr_dev_api:latest .

run-bg: # run all containers in the background
	@docker-compose up -d \
		jr_dev_api \
		mysql

run: # run all containers in the foreground
	@docker-compose up \
		jr_dev_api \
		mysql

logs: # attach to the containers live to view their logs
	@docker-compose logs -f

test: # run the tests
	@docker-compose exec jr_dev_api /scripts/run-tests.sh

test-dbg: # run the tests in debug mode
	@docker-compose exec jr_dev_api /scripts/run-tests.sh --dbg
