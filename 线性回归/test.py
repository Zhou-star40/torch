import os
import sys
import platform
import subprocess
import importlib.util

print("=" * 60)
print("1. 系统与 Python 基础信息")
print("=" * 60)

print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("macOS:", platform.mac_ver())
print("Machine:", platform.machine())
print("Current working directory:", os.getcwd())
print("CONDA_PREFIX:", os.environ.get("CONDA_PREFIX"))
print("CONDA_DEFAULT_ENV:", os.environ.get("CONDA_DEFAULT_ENV"))

print("\n" + "=" * 60)
print("2. PyTorch / MPS 检查")
print("=" * 60)

try:
    import torch

    print("PyTorch version:", torch.__version__)
    print("MPS built:", torch.backends.mps.is_built())
    print("MPS available:", torch.backends.mps.is_available())

    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    print("Selected device:", device)

    x = torch.randn(1000, 1000, device=device, requires_grad=True)
    y = (x @ x).sum()
    y.backward()

    print("Forward result device:", y.device)
    print("Gradient shape:", x.grad.shape)
    print("Gradient device:", x.grad.device)
    print("PyTorch MPS test: PASS")

except Exception as e:
    print("PyTorch MPS test: FAIL")
    print("Error:", repr(e))

print("\n" + "=" * 60)
print("3. 常用深度学习/科学计算库检查")
print("=" * 60)

packages = [
    "numpy",
    "pandas",
    "matplotlib",
    "torch",
    "torchvision",
    "d2l",
    "jupyter",
    "IPython",
]

for pkg in packages:
    spec = importlib.util.find_spec(pkg)
    if spec is None:
        print(f"{pkg}: NOT INSTALLED")
    else:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "version unknown")
            print(f"{pkg}: OK, version = {version}")
        except Exception as e:
            print(f"{pkg}: FOUND BUT IMPORT FAILED -> {repr(e)}")

print("\n" + "=" * 60)
print("4. Jupyter 内核检查")
print("=" * 60)

def run_cmd(cmd):
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=20
        )
        print(f"\n$ {cmd}")
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.stderr.strip():
            print("stderr:", result.stderr.strip())
    except Exception as e:
        print(f"{cmd}: FAILED -> {repr(e)}")

run_cmd("which python")
run_cmd("python --version")
run_cmd("jupyter kernelspec list")

print("\n" + "=" * 60)
print("5. Conda / Miniforge 检查")
print("=" * 60)

run_cmd("which conda")
run_cmd("conda --version")
run_cmd("conda info --envs")

print("\n" + "=" * 60)
print("6. Homebrew 检查")
print("=" * 60)

run_cmd("which brew")
run_cmd("brew --version")
run_cmd("brew doctor")

print("\n" + "=" * 60)
print("7. Xcode / 命令行工具检查")
print("=" * 60)

run_cmd("xcode-select -p")
run_cmd("xcodebuild -version")
run_cmd("clang --version")
run_cmd("git --version")

print("\n" + "=" * 60)
print("检查结束")
print("=" * 60)