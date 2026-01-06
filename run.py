import sys
import os
import subprocess

def main(python):
    with open("./top-200-2025-11-01.txt") as fp:
        succeeded = []
        failed = []
        for idx, line in enumerate(fp):
            package = line.strip()
            print(f"Installing {idx}: {package}")
            os.system("rm -rf .venv")
            os.system(f"uv venv --python {python}")
            retcode = os.system(f"uv pip install --compile-bytecode {package}")
            if retcode == 0:
                succeeded.append(package)
            else:
                failed.append(package)
            if idx == 25:
                break
        # print(succeeded)
        print(failed)

if __name__ == "__main__":
    # main("pypy-3.11.13-linux-x86_64-gnu")
    main("graalpy-3.12.0-linux-x86_64-gnu")
