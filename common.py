import yaml

__config = None

def config():
    global __config

    if not __config:
        with open('./config.yaml', mode='r') as file:
            # Return the config as Json
            __config = yaml.safe_load(file)
    return __config
