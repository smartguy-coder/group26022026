from utils import get_travel_info


message3004 = get_travel_info(driver='Vasyl', passenger_1='Alla', passenger_2='Andriy', passenger_3='Pavlo')
print(message3004)

message0105 = get_travel_info(driver='Vasyl', passenger_1='Alla', passenger_2='Andriy')
print(message0105)

message0105 = get_travel_info(driver='Vasyl', passenger_1="", passenger_2='Andriy')
print(message0105)