from infrastructure import SeoulSubwayAPIClient
from application import GetStationsByLineUseCase

def main():
    api_client = SeoulSubwayAPIClient()
    use_case = GetStationsByLineUseCase(api_client)
    
    stations = use_case.execute(1, 3, "1호선")
    
    for station in stations:
        print(f"""
        역 이름(한글):\t{station.station_nm_kor}
        역 이름(영어):\t{station.station_nm_eng}
        호선:\t{station.line_num}
        """)
        
if __name__ == "__main__":
    main()