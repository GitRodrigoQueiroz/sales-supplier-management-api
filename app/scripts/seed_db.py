import os

import pandas as pd
from sqlalchemy.orm import sessionmaker

from app.models import *
from app.services.db_service import create_db_engine
from app.session import DATABASE_CREDENTIALS

SEED_DIR = "app/seed/"


def get_model_by_name(model_name: str):
    return globals().get(model_name)


def insert_data_from_csv(engine):
    files = sorted(os.listdir(SEED_DIR), key=lambda x: int(x.split(".")[0]))
    for file in files:
        if file.endswith(".csv"):
            with sessionmaker(bind=engine)() as session:
                try:
                    model_name = os.path.splitext(file)[0][2::]
                    model = get_model_by_name(model_name)

                    if not model:
                        print(
                            f"[WARNING] Nenhum modelo encontrado para "
                            f"{model_name}, ignorando..."
                        )
                        continue

                    file_path = os.path.join(SEED_DIR, file)
                    df = pd.read_csv(file_path)

                    records = df.to_dict(orient="records")

                    if records:
                        session.bulk_insert_mappings(model, records)
                        session.commit()
                        print(
                            f"[SUCCESS] Inseridos {len(records)} registros"
                            f" na tabela {model_name}"
                        )
                    else:
                        print(f"[INFO] Nenhum dado encontrado em {file}")

                except Exception as e:
                    session.rollback()
                    print(f"[ERROR] Erro ao inserir dados: {e}")
                finally:
                    session.close()


if __name__ == "__main__":
    engine = create_db_engine(**DATABASE_CREDENTIALS)
    insert_data_from_csv(engine)
