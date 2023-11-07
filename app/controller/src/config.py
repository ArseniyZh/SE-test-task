from environs import Env

env = Env()
env.read_env()

REDIS_HOST = env.str("REDIS_HOST")

MANIPULATOR_HOST = env.str("MANIPULATOR_HOST")
MANIPULATOR_PORT = env.int("MANIPULATOR_PORT")
MANIPULATOR_INTERVAL = env.float("MANIPULATOR_INTERVAL")

DB_HOST = env.str("DB_HOST")
DB_NAME = env.str("DB_NAME")
DB_USERNAME = env.str("DB_USERNAME")
DB_PASSWORD = env.str("DB_PASSWORD")
