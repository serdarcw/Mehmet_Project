from covid import Covid
from datetime import datetime

def info_covid(country):
    covid = Covid()
    result= covid.get_status_by_country_name(country)
    result['last_update'] = datetime.fromtimestamp(result['last_update']//1000)
    return result

print(info_covid('Turkey'))
