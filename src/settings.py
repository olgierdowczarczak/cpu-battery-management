from json import load as jsonload
from subprocess import CalledProcessError, run as subprocessrun

class Settings():
    @classmethod
    def getSettings(cls, file_path: str, key: str, *args) -> None:
        """
        load settings from a JSON file,
        initialize objects based on loaded data
        
        file_path = string, path to JSON file
        key = string, key in JSON object
        *args = string, key in JSON object

        return None
        """
        try:
            with open(file_path) as file:
                settings: dict = jsonload(file)
                for setting in settings[key]:
                    cls(setting, *settings[key][setting].values()) # initialize object
        except FileNotFoundError as path_error: # file does not exists
            print(f"ERROR 1: '{path_error}'")
        except Exception as error: # 
            print(f"ERROR 2: '{error}'") # no expected error
        return None


class EnergySettings(Settings):
    energy_settings: list[object] = []
    energy_active_object :object|None = None
    
    def __init__(self, energy_setting_name: str, energy_battery_usage: int, energy_scheme_name: str, energy_max_cpu: float) -> None:
        """
        Initialize EnergySettings object

        energy_setting_name = string, setting name
        energy_battery_usage = int, battery usage in setting
        energy_scheme_name = string, power scheme name
        energy_max_cpu = float, max cpu usage from one app

        return None
        """
        self.energy_setting_name: str = energy_setting_name
        self.energy_battery_usage: int = energy_battery_usage
        self.energy_scheme_name: str = energy_scheme_name
        self.energy_max_cpu: float = energy_max_cpu
        EnergySettings.energy_settings.append(self)

    @classmethod
    def setEnergySetting(cls, obj: object) -> None:
        """ 
        Changing power plan

        obj = class object 

        return None 
        """
        if cls.energy_active_object == obj:
            return None
        command: str = f"powercfg /SETACTIVE {obj.energy_scheme_name}"
        try:
            subprocessrun(command, shell=True, check=True) # changing plan schema
            print(f"POWER PLAN HAS BEEN CHANGED INTO: '{obj.energy_scheme_name}'")
            cls.energy_active_object = obj # active obj
        except CalledProcessError:
            print(f"ERROR 3: '{CalledProcessError}'!") # return != 0
        return None


class BatterySettings(Settings):
    battery_settings:list[object] = []
    is_battery_plugged:bool = False
    battery_usage:int = False
    
    def __init__(self, battery_energy_status: str, low_energy: bool, medium_enegry: bool, max_energry: bool) -> None:
        """
        Initialize BatterySettings object

        battery_energy_status = string
        low_energy = bool
        medium_enegry = bool
        max_energry = bool

        return None
        """
        self.battery_energy_status: str = battery_energy_status
        self.battery_energy_list: list[bool, bool, bool] = [low_energy, medium_enegry, max_energry]
        BatterySettings.battery_settings.append(self)

def getSettings() -> None:
    """
    load settings from JSON file

    return None
    """
    EnergySettings.getSettings("json/energy_settings.json", "energy_settings", "BATTERY_USAGE", "SCHEME_NAME", "MAX_CPU")
    BatterySettings.getSettings("json/battery_settings.json", "battery_settings", "LOW_ENERGY", "MEDIUM_ENERGY", "MAX_ENERGY")
    return None