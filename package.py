
name = "future"

description = "Clean single-source support for Python 3 and 2"

version = "0.18.2"

requires = []

variants = [
    ["python-2.7"],
]


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
