set -e

usage() {
    echo "Usage: $0 [test|prod]"
    echo "  test: Upload to TestPyPI and install from TestPyPI"
    echo "  prod: Upload to PyPI and install from PyPI"
    exit 1
}

echo "Upgrading pip and installing required packages..."
pip install --upgrade pip
pip install --upgrade setuptools wheel twine

echo "Cleaning up previous builds..."
rm -rf build/ dist/ arden_calculator.egg-info/

echo "Building the package..."
python setup.py sdist bdist_wheel

echo "Uploading the package..."
pip install --index-url $INDEX_URL --no-deps arden_calculator

deactivate

echo "Done!"