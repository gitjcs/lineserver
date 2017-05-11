
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
# E402 is module level import not at top of file
flake8 --ignore=E402 .

if [ $? -ne 0 ] ; then
    echo "flake8 issues."
    exit 1
fi

nosetests tests/

if [ $? -ne 0 ] ; then
    echo "test failures, aborting build."
    exit 1
fi

echo "Success building lineserver."
