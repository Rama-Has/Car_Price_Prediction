from dataclasses import dataclass 

@dataclass
class CarFeatures:
    model: str 
    color: str 
    model_year: float 
    passengers_number: float 
    fuel_type: str
    gear_type: str
    previous_owners: float
    motor_power: float
    trip: float 
    original_type: str 
    license: str   
    glass_type: str 
    airbag: int
    cd_player: int
    alarm: int 
    air_condition: int
    mag_rims: int #جنطات مغنيسيوم
    sunroof: int 
    leather_seats: int 
    closer: int


