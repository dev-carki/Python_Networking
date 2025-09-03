from dataclasses import dataclass

from domain import Subway

@dataclass
class SubwayDTO:
    STATION_CD: str
    STATION_NM: str
    STATION_NM_ENG: str
    LINE_NUM: str
    FR_CODE: str
    STATION_NM_CHN: str
    STATION_NM_JPN: str
    
    @staticmethod
    def from_dict(data: dict) -> "SubwayDTO":
        return SubwayDTO(
            STATION_CD=data["STATION_CD"],
            STATION_NM=data["STATION_NM"],
            STATION_NM_ENG=data["STATION_NM_ENG"],
            LINE_NUM=data["LINE_NUM"],
            FR_CODE=data["FR_CODE"],
            STATION_NM_CHN=data["STATION_NM_CHN"],
            STATION_NM_JPN=data["STATION_NM_JPN"],
        )

    def to_domain(self) -> Subway:
        return Subway(
            # code=self.STATION_CD,
            station_nm_kor=self.STATION_NM,
            station_nm_eng=self.STATION_NM_ENG,
            line_num=self.LINE_NUM,
        )