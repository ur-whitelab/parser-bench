import re
import json

def parse_res_zeopp(filecontent: str):
    """Parse the results line of a network -res call to zeopp
    Args:
        filecontent (str): results file
    """
    first_line = filecontent.split("\n")[0]
    parts = first_line.split()

    results = {
        "lis": float(parts[1]),  # largest included sphere
        "lifs": float(parts[2]),  # largest free sphere
        "lifsp": float(parts[3]),  # largest included sphere along free sphere path
    }

    return json.dumps(results)
