#!make

launch-db:
	docker-compose up -d

create-db:
	python3 -m app.scripts.create_db

seed-db:
	python3 -m app.scripts.seed_db

launch-api:
	uvicorn app:app --reload