#!/usr/bin/python3.12
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 frank yang
#
# @Time    : 2024/2/10 10:39
# @Author  : frank yang
# @File    : check_cpu_gpu.py
# @IDE     : PyCharm


import os
import pprint
import subprocess


def get_cpu_temperature():
    try:
        # Execute the 'wmic' command to get CPU temperature
        result = subprocess.check_output("wmic /namespace:\\\\root\\cimv2 PATH Win32_PerfFormattedData_Counters_ThermalZoneInformation get Temperature", shell=True)
        # Extract the temperature from the result
        temperature_str = result.decode("utf-8").split("\n")[1].strip()
        temperature = float(temperature_str) / 10.0
        return temperature
    except Exception as e:
        print("Error:", e)
        return None

def get_gpu_temperature():
    temperature = None
    try:
        # Execute the 'nvidia-smi' command to get GPU temperature
        result = os.popen("nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader").read()
        # Extract the temperature from the result
        temperature = float(result.strip())
    except Exception as e:
        print("Error:", e)
    return temperature


cpu_temperature = get_cpu_temperature()
gpu_temperature = get_gpu_temperature()

if cpu_temperature is not None:
    print("CPU Temperature:", cpu_temperature, "°C")
else:
    print("Failed to retrieve CPU temperature")

if gpu_temperature is not None:
    print("GPU Temperature:", gpu_temperature, "°C")
else:
    print("Failed to retrieve GPU temperature")
