## check if Python venv exists
if [ ! -d ".venv" ]; then
    echo "Creating Python venv..."
    python3 -m venv .venv
fi

## activate Python venv
echo "Activating Python venv..."
source .venv/bin/activate

## install Python dependencies
echo "Installing Python dependencies..."
pip install poetry
poetry install

## activate pre-commit hooks
echo "Activating pre-commit hooks..."
pre-commit install
