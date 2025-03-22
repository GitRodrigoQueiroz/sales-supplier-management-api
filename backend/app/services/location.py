from fastapi import HTTPException, status
from sqlalchemy import insert, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.models import Location
from backend.app.schemas import (
    LocationCreate,
    LocationUpdate,
)


class LocationUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def bulk_insert_locations(self, locations: list[LocationCreate]):
        data_list = [location.dict() for location in locations]
        try:
            self.db_session.execute(insert(Location), data_list)
            self.db_session.commit()
            return {"message": f"{len(locations)} locations inserted successfully"}
        except IntegrityError:
            self.db_session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Some locations already exist",
            )

    # # 🔵 RETRIEVAL - Buscar localizações por um critério (ex: país)
    # def get_locations_by_country(self, country: str, limit: int = 100):
    #     locations = (
    #         self.db_session.query(Location)
    #         .filter(Location.country == country)
    #         .limit(limit)
    #         .all()
    #     )
    #     if not locations:
    #         raise HTTPException(
    #             status_code=status.HTTP_404_NOT_FOUND,
    #             detail="No locations found for this country",
    #         )
    #     return locations

    def bulk_delete_locations(self, location_ids: list[int]):
        if not location_ids:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No location IDs provided for deletion",
            )

        try:
            # Deleta os registros com location_id dentro da lista fornecida
            rows_deleted = (
                self.db_session.query(Location)
                .filter(Location.location_id.in_(location_ids))  # Usando .in_()
                .delete(synchronize_session="fetch")  # Deleta em bulk
            )

            # Verifica se nenhum registro foi deletado
            if rows_deleted == 0:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No locations found to delete",
                )

            self.db_session.commit()
            return {"message": f"{rows_deleted} locations deleted successfully"}

        except Exception as e:
            self.db_session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error deleting locations: {str(e)}",
            )

    def bulk_update_locations(self, locations: list[LocationUpdate]):
        if not locations:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No locations provided for update",
            )

        try:
            for location_data in locations:
                self.db_session.execute(
                    update(Location)
                    .where(Location.location_id == location_data.location_id)
                    .values(location_data.data.dict(exclude_unset=True))
                )

            self.db_session.commit()
            return {"message": f"{len(locations)} locations updated successfully"}
        except Exception as e:
            self.db_session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error updating locations: {str(e)}",
            )
