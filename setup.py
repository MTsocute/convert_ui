from setuptools import setup

setup(
    name="convert_ui",
    version='0.3.2',
    py_modules=['convert_ui'],
    description="Convert Python to Qt Ui File",
    install_requires=[
        'pyside6==6.9.2',
        'rich==14.1.0',
        'rich-argparse==1.7.1'
    ],
    entry_points={
        'console_scripts': [
            'convert_ui=convert_ui:main',  # 运行 convert_ui.py 脚本的 main()
        ]
    }
)
