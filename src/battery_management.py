from settings import EnergySettings, BatterySettings

def getEnergySetting() -> None:
    """
    Determine and set the appropriate energy setting based on battery level and plugged status

    return None
    """
    # check if battery in in acceptable range
    if not 1 <= BatterySettings.battery_usage <= 100:
        print(f"BATTERY LEVEL EXCEEDED LIMIT ('{BatterySettings.battery_usage}'%)")
        return None
        
    # get battery settings depends on battery plugged status
    battery:BatterySettings = BatterySettings.battery_settings[BatterySettings.is_battery_plugged]
    
    # determine length of energy list
    new_list_length:int = -1
    for index, setting in enumerate(EnergySettings.energy_settings):
        if battery.battery_energy_list[index]:
            new_list_length += 1
    
    # search for index from list which is setting index from EnergySettings.energy_settings
    list_index:int = -1
    for index in range(new_list_length + 1):
        if BatterySettings.battery_usage >= EnergySettings.energy_settings[index].energy_battery_usage:
            list_index += 1
        else:
            list_index += 1
            break
    
    # Set energy setting
    EnergySettings.setEnergySetting(EnergySettings.energy_settings[list_index])
    return None

def managementBattery(battery) -> None:
    """
    Manage battery

    battery = psutil object

    return None
    """
    # update battery status and usage
    BatterySettings.is_battery_plugged = battery.power_plugged
    BatterySettings.battery_usage = battery.percent

    # get and set energy setting
    return getEnergySetting()