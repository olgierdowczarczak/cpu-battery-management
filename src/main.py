from settings import getSettings, BatterySettings, EnergySettings
from cpu_management import managementCPU
from battery_management import managementBattery
from psutil import Process, sensors_battery, cpu_percent


def main() -> None:
    """
    Main function to manage CPU and battery

    return None
    """
    # current process ID
    active_pid: int = Process().pid
    
    # main loop to monitor battery and CPU
    while True:
        # manage battery
        managementBattery(sensors_battery())

        #manage CPU
        managementCPU(cpu_percent(interval=1), active_pid)
    return None

if __name__ == "__main__":
    # load settings
    getSettings()
    
    # call function
    main()