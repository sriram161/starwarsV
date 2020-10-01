import yaml

def get_config(pattern):
    with open('./configs/settings.yaml') as fp:
        settings = yaml.load(fp)
    return settings[pattern]

def get_starwars_url():
    return get_config('urls')['starwars_api']
