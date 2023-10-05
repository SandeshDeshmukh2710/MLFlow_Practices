import sysconfig
import os

def get_virtual_env_name():
    env_path = sysconfig.get_paths()["purelib"]
    env_name = env_path.split(os.sep)[-2]
    return env_name

if __name__ == "__main__":
    env_name = get_virtual_env_name()
    print(f"Currently active virtual environment: {env_name}")
