import subprocess
import sys

# Function to install packages
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install nicegui
install_package("nicegui")