import os
import requests
from typing import List

from domain import Subway
from data import SubwayDTO

class SeoulSubwayAPIClient:
    BASE_URL = "http://openapi.seoul.go.kr:8088"
    API_KEY = os.environ.get("SEOUL_API_KEY")
    
    def get_stations(
        self, 
        start_index: int, 
        end_index: int, 
        line: str, 
        station_code: str = "", 
        station_name: str = ""
    ) -> List[Subway]:
        url = (
            f"{self.BASE_URL}/{self.API_KEY}/json/SearchSTNBySubwayLineInfo/"
            f"{start_index}/{end_index}/{station_code}/{station_name}/{line}"
        )
        response = requests.get(url=url)
        response.raise_for_status()
        
        data = response.json()
        rows = data["SearchSTNBySubwayLineInfo"]["row"]
        
        dtos = [SubwayDTO.from_dict(row) for row in rows]
        stations = [dto.to_domain() for dto in dtos]
        
        return stations