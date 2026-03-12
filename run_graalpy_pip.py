import sys
import os
import subprocess

def main(python, jit=False):
    with open("./top-300-2025-11-01.txt") as fp:
        succeeded = []
        failed = []
        for idx, line in enumerate(fp):
            package = line.strip()
            print(f"Installing {idx}: {package}")
            os.system("rm -rf .venv")
            os.system(f"uv venv --python {python}")
            os.system(f".venv/bin/python -m ensurepip")
            retcode = os.system(f".venv/bin/python -m pip install -r ./requirements/{package}.txt")
            if retcode == 0:
                succeeded.append(package)
            else:
                failed.append(package)
        with open(f"{python}-graalpy-pip.txt", "w") as fp:
            fp.write(f"{len(succeeded)}\n")
            fp.write(f"{succeeded}\n")
            fp.write(f"{len(failed)}\n")
            fp.write(f"{failed}\n")

if __name__ == "__main__":
    # GraalPy:
    main("graalpy-3.12.0-linux-x86_64-gnu")
