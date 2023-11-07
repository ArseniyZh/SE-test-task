from environs import Env

env = Env()
env.read_env()

MANIPULATOR_HOST = env.str("MANIPULATOR_HOST")
MANIPULATOR_PORT = env.int("MANIPULATOR_PORT")
