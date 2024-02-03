import os

# Gets the path to a resource file, works in production and development
# _MEIPASS2 is the directory that resource files are packed into upon compilation/bundling
def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )