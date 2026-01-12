import sys
import os
import subprocess

FREEZE = False

def main(python, jit=False):
    jit_str = "PYTHON_JIT=1" if jit else ""
    with open("./top-300-2025-11-01.txt") as fp:
        succeeded = []
        failed = []
        for idx, line in enumerate(fp):
            package = line.strip()
            print(f"Installing {idx}: {package}")
            os.system("rm -rf .venv")
            os.system(f"uv venv --python {python}")
            if FREEZE:
                retcode = os.system(f"{jit_str} uv pip install {package}")
            else:
                retcode = os.system(f"{jit_str} uv pip install -r ./requirements/{package}.txt")
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
    # Baseline: CPython compiled with all DSL-assisted optimizations on.
    main("cpython-3.14.2-linux-x86_64-gnu", jit=True)

    # PyPy:
    main("pypy-3.11.13-linux-x86_64-gnu")

    # GraalPy:
    main("graalpy-3.12.0-linux-x86_64-gnu")
