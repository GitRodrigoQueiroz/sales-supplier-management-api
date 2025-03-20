#!make

launch-db:
	docker-compose up

create-db:
	python3 -m backend.app.scripts.create_db

seed-db:
	python3 -m backend.app.scripts.seed_db