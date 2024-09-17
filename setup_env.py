import os
import subprocess
import sys
from appium import webdriver
from appium.options.android import UiAutomator2Options

def install_dependencies():
    # Install required Python dependencies
    print("Installing required Python packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def install_apk():
    # Install APK on the connected Android device
    apk_path = os.path.join(os.getcwd(), "apk", "smmr1.apk")
    
    print(f"Installing APK: {apk_path}")
    result = subprocess.run(["adb", "install", apk_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        print("APK installed successfully!")
    else:
        print(f"Error installing APK: {result.stderr.decode('utf-8')}")

def setup_environment():
    # Set up environment (install dependencies, APK, etc.)
    install_dependencies()
    install_apk()

def launch_appium_and_run_tests():
    # Assuming Appium server is already running
    print("Running tests...")
    subprocess.run(["behave"])

if __name__ == "__main__":
    setup_environment()
    launch_appium_and_run_tests()
