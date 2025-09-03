from typing import List

from domain import Subway
from infrastructure import SeoulSubwayAPIClient

class GetStationsByLineUseCase:
    def __init__(self, api_client: SeoulSubwayAPIClient):
        self.api_client = api_client

    def execute(
        self, 
        start_index: int, 
        end_index: int, 
        line: str, 
        station_code: str = "", 
        station_name: str = ""
    ) -> List[Subway]:
        return self.api_client.get_stations(start_index, end_index, line, 
                                            station_code, station_name)