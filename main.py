from typing import Generator, Dict

def read_ini(path: str) -> Generator:
    """Read ini configuration file

    Args:
        path (str): file path

    Raises:
        e: IOError

    Yields:
        Generator: each line of the configuration
    """
    try:
        with open(path, "r") as fh:
            lines = fh.readlines()
            for line in lines:
                yield line.strip("\n")
    except FileNotFoundError as e:
        raise e


def parse_ini(path: str) -> Dict[str, Dict[str, str]]:
    """Parse INI configuration file

    Args:
        path (str): file path

    Returns:
        Dict[Dict[str, str]]: INI configuration file as dictionary
    """
    config = {}
    current_section = None
    for line in read_ini(path):
        if line == "" or line.startswith(";"):
            # skip blank lines and comments
            continue
        if line.startswith("[") and line.endswith("]"):
            current_section = line.strip("[]")
            config[current_section] = {}
            continue

        key, val = line.split("=", 1)

        if current_section is not None:
            config[current_section][key.strip()] = val.strip()
            continue
        else:
            config[key.strip()] = val.strip()
            current_section = None
    return config

if __name__ == "__main__":
    print(parse_ini("samples/sample.ini"))
    print(parse_ini("samples/generic.ini"))