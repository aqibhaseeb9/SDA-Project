
from functools import reduce

def Statistical_Analysis(filtered_data,config,operation):
    if operation=='Sum':
        return Sum_gdp_region(filtered_data,config)
    elif operation=='Average':
        return Avg_gdp_region(filtered_data,config)

    


def Sum_gdp_region(filtered_data,config):

    continents = [c.strip() for c in config.get("continent").split("&")]
    
    filtered_sum_region = filter(
            lambda row:row['continent'] in continents and 
            row['gdp'] is not None,
            filtered_data
            )
    
    gdp_values = list(map(lambda row:row['gdp'],filtered_sum_region))
    
    return reduce(lambda a,b:a+b,gdp_values,0)

def Avg_gdp_region(filtered_data,config):
    return Sum_gdp_region(filtered_data,config)/float(len(filtered_data))

def Avg_gdp_Country(filtered_data,config):

    country = [c.strip() for c in config.get("country")]
    
    filtered_sum_region = filter(
            lambda row:row['country'] in country and 
            row['gdp'] is not None,
            filtered_data
            )
    
    gdp_values = list(map(lambda row:row['gdp'],filtered_sum_region))
    
    sum = reduce(lambda a,b:a+b,gdp_values,0)
    return sum/float(len(filtered_data))