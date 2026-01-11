import sys
import os
import subprocess

FREEZE = False

def main(python):
    with open("./top-200-2025-11-01.txt") as fp:
        succeeded = []
        failed = []
        for idx, line in enumerate(fp):
            package = line.strip()
            print(f"Installing {idx}: {package}")
            os.system("rm -rf .venv")
            os.system(f"uv venv --python {python}")
            retcode = os.system(f"PYTHON_JIT=1 uv pip install --compile-bytecode {package}")
            if retcode == 0:
                succeeded.append(package)
                if FREEZE:
                    os.system(f"uv pip freeze > ./requirements/{package}.txt")
            else:
                failed.append(package)
        with open(f"{python}.txt", "w") as fp:
            fp.write(f"{len(succeeded)}\n")
            fp.write(f"{succeeded}\n")
            fp.write(f"{len(failed)}\n")
            fp.write(f"{failed}\n")

if __name__ == "__main__":
    main("cpython-3.14.2-linux-x86_64-gnu")
    # main("pypy-3.11.13-linux-x86_64-gnu")
    # main("graalpy-3.12.0-linux-x86_64-gnu")
