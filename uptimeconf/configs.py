import environ

env = environ.Env()

env.read_env('.env')


def __get_env_variable(key: str, default_value=None) -> str:
    return env(key, default=default_value)


configs = {
    'SECRET_KEY': __get_env_variable('SECRET_KEY', 'HALA_LALAY_LALAY_LA_LA_LAY_LAAY'),
    'DEBUG': __get_env_variable('DEBUG', 'True'),
    'ALLOWED_HOSTS': __get_env_variable('DJANGO_ALLOWED_HOSTS', '127.0.0.1 localhost [::1]').split(' '),
}

def get_config(config_name):
    return configs.get(config_name)