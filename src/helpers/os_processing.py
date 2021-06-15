import os
def prep_packages(data):
    for package in data:
        # print(package)
        os.system(f"pip3 install -Iv {package}=={data[package]}")
