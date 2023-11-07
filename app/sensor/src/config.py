from environs import Env

env = Env()
env.read_env()

SENSOR_COUNT = env.int("SENSOR_COUNT")
MESSAGES_PER_SECOND = env.int("MESSAGES_PER_SECOND")
CONTROLLER_URL = env.str("CONTROLLER_URL")
