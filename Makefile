#!make

launch-db:
	docker-compose up

create-database:
	python3 -m backend.app.db.create_db

seed-db:
	