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


valid_columns_names = {
    'model': 'الموديل',
    'model_year': 'موديل سنة',
    'color': 'لون السيارة',
    'motor_power': 'قوة الماتور',
    "passengers_number":'عدد الركاب',
    "trip": 'عداد السيارة',
    "previous_owners":'أصحاب سابقون',
    "original_type":'أصل السيارة',
    "license": 'رخصة السيارة',
    "fuel_type":'نوع الوقود',
    "gear_type":'نوع الجير',
    "glass_type":'الزجاج',
    "airbag": 'وسادة حماية هوائية',
    "leather_seats":'فرش جلد',
    "mag_rims":'جنطات مغنيسيوم',
    "sunroof": 'فتحة سقف',
    "cd_player":'مسجل CD',
    "closer": 'إغلاق مركزي',
    "air_condition": 'مُكيّف',
    "alarm": "جهاز إنذار"
} 

