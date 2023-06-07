import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

    __version__ = "0.0.0"

    REPO_NAME = "text-summarization"
    AUTHOR = "Neda Ebrahimi"
    SRC_REPO = "textSummarizer"


    setuptools.setup(
            name=REPO_NAME,
            version=__version__,
            author=AUTHOR,
            author_email="neda.ebrahimi.kp@gmail.com",
            description="Text summarization",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/neda60/text-summarization",
            packages=setuptools.find_packages()
    )

