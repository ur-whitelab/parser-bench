import re
import json

def parse_sa_zeopp(filecontent):
    regex_unitcell = re.compile(r"Unitcell_volume: ((\d+\.\d+)|\d+)|$")
    regex_density = re.compile(r"Density: ((\d+\.\d+)|\d+)|$")
    asa_a2 = re.compile(r"ASA_A\^2: ((\d+\.\d+)|\d+)|$")
    asa_m2cm3 = re.compile(r"ASA_m\^2/cm\^3: ((\d+\.\d+)|\d+)|$")
    asa_m2g = re.compile(r"ASA_m\^2/g: ((\d+\.\d+)|\d+)|$")
    nasa_a2 = re.compile(r"NASA_A\^2: ((\d+\.\d+)|\d+)|$")
    nasa_m2cm3 = re.compile(r"NASA_m\^2/cm\^3: ((\d+\.\d+)|\d+)|$")
    nasa_m2g = re.compile(r"NASA_m\^2/g: ((\d+\.\d+)|\d+)|$")

    d = {
        "unitcell_volume": float(re.findall(regex_unitcell, filecontent)[0][0]),
        "density": float(re.findall(regex_density, filecontent)[0][0]),
        "asa_a2": float(re.findall(asa_a2, filecontent)[0][0]),
        "asa_m2cm3": float(re.findall(asa_m2cm3, filecontent)[0][0]),
        "asa_m2g": float(re.findall(asa_m2g, filecontent)[0][0]),
        "nasa_a2": float(re.findall(nasa_a2, filecontent)[0][0]),
        "nasa_m2cm3": float(re.findall(nasa_m2cm3, filecontent)[0][0]),
        "nasa_m2g": float(re.findall(nasa_m2g, filecontent)[0][0]),
    }

    return json.dumps(d)
