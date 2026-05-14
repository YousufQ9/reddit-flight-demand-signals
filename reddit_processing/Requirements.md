1. Downloading the Reddit Datasets

   1. Install a torrent client

      * Example: qBittorrent or any similar client
   2. Download torrent from:

      * https://academictorrents.com/details/3e3f64dee22dc304cdd2546254ca1f8e8ae542b4
   3. Select and download the following files:

      * subreddits25/Europetravel\_submissions.zst (15.97 MB)
      * subreddits25/uktravel\_submissions.zst (10.10 MB)
      * subreddits25/travel\_submissions.zst (417.91 MB)
      * subreddits25/solotravel\_submissions.zst (56.59 MB)
      * subreddits25/backpacking\_submissions.zst (57.41 MB)
   4. Install required python library: Run pip install zstandard
   5. Decompress from .zst to .csv:

      * File path of to\_csv.py: Set 'base\_path' (Line 16) to directory containing all subreddit .zst files 
      * The to\_csv.py file is from: https://github.com/Watchful1/PushshiftDumps/blob/master/scripts/to\_csv.py with some edits
   6. Run AllFileScript.py:

      * Execute AllFileScript.py to process all files and generate CSV outputs (Appx 280 MB)

2. Extract locations + Sentiment

   1. Run SubredditCleaning.ipynb:
      * Keep this file in the same folder as the reddit datasets.
      * Change the file path to file you want to process. Example: file_path = BASE_DIR / "uktravel_submissions.csv"
   2. Run city-country recognition.ipynb:
      * Install required python libraries:
       Run pip install pandas spacy geonamescache pycountry unidecode vaderSentiment openpyxl
      * Change input file name to file you want to process. Example: df = pd.read_csv("travel_processed.csv")

3. Merge SubReddit Datasets into 1 Large Dataset

   1. Run RedditMerge.ipynb:
      * Keep this file in the same folder as the processed reddit datasets.
      * Change the file names as appropriate.
 


