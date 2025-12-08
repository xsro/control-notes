import sys
import subprocess
from pathlib import Path


def run_script(filename):
    subprocess.run([sys.executable,filename],cwd=Path(__file__).parent)


if __name__=="__main__":
    for file in Path(__file__).parent.glob("*.py"):
        if file == Path(__file__):
            continue
        print(file)
        run_script(file)