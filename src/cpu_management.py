from settings import EnergySettings, BatterySettings
from psutil import process_iter, cpu_percent, Process, AccessDenied

def managementCPU(cpu_usage: float, active_pid: int) -> None:
    """
    Description: Manage CPU usage by terminating processes that exceed the maximum CPU threshold set in Energy Settings

    params:
    cpu_usage = float, Current CPU usage in %
    active_pid = int, PID of active process

    return None
    """
    # check if active energy setting is defined
    if EnergySettings.energy_active_object is None:
        return None

    # iterate all running processes
    all_processes = process_iter()
    for proc in all_processes:
        # CPU usage from process
        proc_usage = proc.cpu_percent()
        # check if process exceeds maximum CPU threshold
        if proc.pid and proc_usage > EnergySettings.energy_active_object.energy_max_cpu:
            # skip active pid
            if proc.pid == active_pid:
                continue
            try:
                # attempt to terminate process
                kill_proc = Process(proc.pid)
                print(f"PID '{proc.pid}' HAS BEEN KILLED")
                kill_proc.terminate()
            except AccessDenied:
                # process can not be terminated
                continue
    return None