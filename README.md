# Setup env Shell/Terminal

## Install virtualenv if not already installed
pip install virtualenv

## Navigate to project directory
cd path\to\project\directory

## Create a virtual environment
python -m venv venv  # Windows
## or
python3 -m venv venv  # macOS/Linux

## Activate the virtual environment
venv\Scripts\activate  # Windows
## or
source venv/bin/activate  # macOS/Linux

## Install required packages
pip install -r requirements.txt

# Setup env Anaconda

## Create a new conda environment named 'myenv' with Python 3.11
conda create --name myenv python=3.11

## Activate the environment
conda activate myenv

## Install required packages from the requirements.txt file
pip install -r requirements.txt


# Running Streamlit

streamlit run dashboard/dashboard.py
