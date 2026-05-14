# reddit-flight-demand-signals
Analysing Reddit travel engagement as a leading indicator of European flight booking surges, including: NLP pipeline, STL deseasonalization, relevance scoring across 41 countries.

# Reddit Signal Analysis Pipeline

Analyses the relationship between Reddit social media engagement and European flight booking data, investigating whether Reddit signals can serve as leading indicators of airline booking surges.

> **Note:** The Lufthansa proprietary booking dataset (~45M rows) is confidential and not included in this repository. See [Data](#data) for details.

---

## Background

This project was developed as part of a semester-long practicum with Lufthansa Group's Europe division. The central question: can social media engagement, specifically Reddit activity across travel-focused communities, predict surges in European flight bookings ahead of time?

The key methodological finding was that ~60% of the apparent raw correlation between Reddit engagement and flight bookings (raw Spearman r = 0.71–0.79) was attributable to shared weekly seasonality rather than genuine predictive signal. After STL deseasonalization, correlations dropped substantially but began to decay with lag, confirming genuine temporal directionality. Following a Reddit engagement spike, the probability of a booking spike within 14 days was **15.2%** which was a 9× increase over the 1.7% base rate.

---

## Pipeline Structure

| Notebook | Purpose |
|---|---|
| `1_loading.ipynb` | CSV to Parquet conversion, LHG schema validation, Reddit loading, destination matching pipeline, daily panel creation |
| `2_featureengineering.ipynb` | Date spine filling, rolling window features, spike detection, sentiment & engagement features, lag features, panel join |
| `3_laganalysis.ipynb` | CCF analysis, Spearman correlations, deseasonalization correction, spike co-occurrence, sentiment vs consistent sentiment comparison |
| `4_relevancescore.ipynb` | Feature normalisation, three scoring approaches (weighted linear, sentiment-first, momentum), evaluation, dynamic country ranking |
| `5_VARprediction.ipynb` | Stationarity testing, Granger causality tests (all 41 countries), VAR forecasting — ultimately not used in final analysis |

### Run Order

Notebooks must be run in sequence as each depends on outputs from the previous:

```
1_loading.ipynb
        ↓
2_featureengineering.ipynb
        ↓
3_laganalysis.ipynb
        ↓
4_relevancescore.ipynb
        ↓
5_VARprediction.ipynb
```

---

## Setup

```bash
pip install -r requirements.txt
```

Then install the spaCy language model:

```bash
python -m spacy download en_core_web_sm
```

---

## Configuration

Before running any notebook, update the three path variables in the first cell of **each notebook**:

```python
FOLDER_PATH  = Path(r"path/to/your/data")      # folder containing raw CSVs and Reddit CSV
PARQUET_DIR  = Path(r"path/to/your/parquet")    # where converted Parquet files are stored
OUTPUT_PATH  = Path(r"path/to/your/outputs")    # where all outputs and figures are saved
```

`PARQUET_DIR` and `OUTPUT_PATH` are created automatically if they don't exist. `FOLDER_PATH` must already exist and contain the raw data files listed below.

---

## Data

### Lufthansa Booking Data (Confidential — Not Included)

The Lufthansa proprietary dataset covered ~45M rows of daily flight transactions across ~8,000 city-pairs to and from Europe (December 2024 – December 2025). This data was provided under NDA and **cannot be shared**.

The pipeline expects the following CSV files in `FOLDER_PATH`:

| Filename | Description |
|---|---|
| `DACHBE-DACHBE.csv` | DACH/Benelux to DACH/Benelux routes |
| `DACHB-EU.csv` | DACH/Benelux to broader Europe routes |
| `EU-DACHB.csv` | Europe to DACH/Benelux routes |
| `EU-EU.csv` | Europe to Europe routes |

### Reddit Data

Reddit data was sourced from [Academic Torrents](https://academictorrents.com/details/3e3f64dee22dc304cdd2546254ca1f8e8ae542b4) due to API access limitations. See [`Requirements.md`](in reddit_processing) for full download and processing instructions.

Five travel subreddits were used, covering January 2024 – December 2025:

| Subreddit | File | Size |
|---|---|---|
| r/EuropeTravel | `Europetravel_submissions.zst` | 15.97 MB |
| r/UKTravel | `uktravel_submissions.zst` | 10.10 MB |
| r/Travel | `travel_submissions.zst` | 417.91 MB |
| r/SoloTravel | `solotravel_submissions.zst` | 56.59 MB |
| r/Backpacking | `backpacking_submissions.zst` | 57.41 MB |

Once downloaded and decompressed (see `Requirements.md`), place the resulting `reddit.csv` in `FOLDER_PATH`.

---

## Key Results

- **41 of 221** unique Reddit destinations were successfully matched to Lufthansa ISO country codes (41.9% of Reddit rows)
- **Deseasonalization is critical:** raw correlations of r = 0.71–0.79 dropped to r ≈ 0.20 after removing shared weekly seasonality
- **Best relevance scoring approach:** Weighted Linear (Approach A) achieved AUC = 0.613 across all 41 countries, rising to **AUC = 0.842** for the 8 highest-signal markets 
- **Granger causality** confirmed significant Reddit -> bookings signal in 7 of 41 countries
- **Booking spike probability** following a Reddit engagement spike: 15.2% within 14 days (vs. 1.7% base rate)

---

## Skills & Tools

Python · pandas · polars · VADER sentiment analysis · spaCy NER · pycountry · RapidFuzz · STL deseasonalization · Spearman correlation · Cross-Correlation Function (CCF) · Granger causality · MinMax normalisation · rolling window features · spike detection (z-score) · AUC/PR-AUC · scikit-learn · matplotlib · statsmodels
