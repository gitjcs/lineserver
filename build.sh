
BASEDIR="$( cd "$( dirname "$0" )" && pwd )"

# Make sure pip is installed
which pip > /dev/null
if [ $? -eq 1 ] ; then
    echo 'pip must be installed (https://packaging.python.org/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers)'
    exit 1
fi

# Install dependencies
pip install -r $BASEDIR/requirements.txt
if [ $? -ne 0 ] ; then
    echo "pip install failed, bailing out"
    exit 1
fi

# Run unit tests
flake8 .

if [ $? -ne 0 ] ; then
    echo "flake8 issues."
    exit 1
fi
