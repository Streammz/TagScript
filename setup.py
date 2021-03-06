from distutils.core import setup

setup(
    name="TagScriptEngine",
    url="https://github.com/JonSnowbd/TagScript/tree/v2",
    author="PySnow",
    author_email="vasti009@gmail.com",
    version="2.1.1",
    packages=[
        "TagScriptEngine",
        "TagScriptEngine.adapter",
        "TagScriptEngine.block",
        "TagScriptEngine.interface",
        "TagScriptEngine.sugar"
    ],
)