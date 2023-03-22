import re
import json

def parse_volpo_zeopp(filecontent):
    regex_unitcell = re.compile(r"Unitcell_volume: ((\d+\.\d+)|\d+)|$")
    regex_density = re.compile(r"Density: ((\d+\.\d+)|\d+)|$")
    av_a3 = re.compile(r"AV_A\^3: ((\d+\.\d+)|\d+)|$")
    av_volume_fraction = re.compile(r"AV_Volume_fraction: ((\d+\.\d+)|\d+)|$")
    av_cm3g = re.compile(r"AV_cm\^3/g: ((\d+\.\d+)|\d+)|$")
    nav_a3 = re.compile(r"NAV_A\^3: ((\d+\.\d+)|\d+)|$")
    nav_volume_fraction = re.compile(r"NAV_Volume_fraction: ((\d+\.\d+)|\d+)|$")
    nav_cm3g = re.compile(r"NAV_cm\^3/g: ((\d+\.\d+)|\d+)|$")

    d = {
        "unitcell_volume": float(re.findall(regex_unitcell, filecontent)[0][0]),
        "density": float(re.findall(regex_density, filecontent)[0][0]),
        "av_a3": float(re.findall(av_a3, filecontent)[0][0]),
        "av_volume_fraction": float(re.findall(av_volume_fraction, filecontent)[0][0]),
        "av_cm3g": float(re.findall(av_cm3g, filecontent)[0][0]),
        "nav_a3": float(re.findall(nav_a3, filecontent)[0][0]),
        "nav_volume_fraction": float(re.findall(nav_volume_fraction, filecontent)[0][0]),
        "nav_cm3g": float(re.findall(nav_cm3g, filecontent)[0][0]),
    }

    return json.dumps(d)