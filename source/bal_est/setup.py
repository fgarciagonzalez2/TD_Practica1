from setuptools import setup

setup(
    name="actividad_final_pa",
    version= "0.0.1",
    packages=["config","enlace_app","api_esios","api_aemet"],
    entry_points={
                "console_scripts": [
                "actividad_final_pa = actividad_final_pa.__main__:main"    
                ]
            },
    install_requires=[]
    )