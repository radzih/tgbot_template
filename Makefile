py := poetry run
python := $(py) python

dirs := project

.ONESHELL:

define setup_env
    $(eval ENV_FILE := $(1))
    @echo " - setup env $(ENV_FILE)"
    $(eval include $(1))
    $(eval export)
endef

.PHONY: reformat
reformat:
	poetry run black $(project)
	poetry run isort $(project) 

.PHONY: dev-bot
dev-bot:
	$(call setup_env, .env.dev)
	$(python) -m project.present.bot

.PHONY: dev-docker
dev-docker:
	docker compose -f=docker-compose-dev.yml --env-file=.env.dev up

.PHONY: dev-migrate
dev-migrate:
	$(call setup_env, .env.dev)
	$(py) alembic upgrade head

.PHONY: dev-env
dev-env:
	$(call setup_env, .env.dev)
	$(filter-out $@,$(MAKECMDGOALS))
