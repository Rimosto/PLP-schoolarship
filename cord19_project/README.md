# CORD-19 Research Papers Data Explorer

This project explores the [CORD-19 dataset](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge).

## Project Structure
- `data/metadata.csv` → Place the downloaded dataset here.
- `notebooks/analysis.ipynb` → Jupyter Notebook for exploration and cleaning.
- `app/app.py` → Streamlit app for interactive exploration.
- `requirements.txt` → Python dependencies.

## Setup Instructions
1. Clone or unzip this project.
2. Download `metadata.csv` from Kaggle and place it into `data/`.
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Run Jupyter Notebook for analysis:
   ```bash
   jupyter notebook notebooks/analysis.ipynb
   ```
5. Start the Streamlit app:
   ```bash
   streamlit run app/app.py
   ```
