# Google Trends Keyword Analyzer (Iran Geo-Targeted)

This Python script utilizes the `pytrends` library to fetch and analyze trending search queries related to a specific keyword within the Iranian region over the last 7 days. It categorizes results into **Top** (most searched) and **Rising** (fastest growing) queries.

## 🚀 Features
* **Geo-Specific:** Hardcoded to track trends within Iran (`geo='IR'`).
* **Localized Language:** Configured with `hl='fa'` for better Persian (Farsi) keyword recognition.
* **Real-time Data:** Fetches the last 7 days of search data.
* **JSON Output:** Formats the SEO data into a clean JSON structure for easy integration with other tools.

## 🛠 Prerequisites

Before running the script, ensure you have the following installed:

* **Python 3.x**
* **pytrends library:**
* ```bash
    pip install pytrends
    ```
* **pandas library:** (Required by pytrends)
    ```bash
    pip install pandas
    ```

## 💻 Usage

1.  Clone or copy the script to your local machine.
2.  Set your desired keyword in the `keyword` variable.
3.  Run the script:
    ```bash
    python your_script_name.py
    ```

## 📊 Logic Overview

The script follows these steps to process SEO data:

1.  **Initialization:** Sets up `TrendReq` with Persian language support and Iran's timezone offset.
2.  **Payload Building:** Requests data for the keyword specifically for the `IR` (Iran) region and a `now 7-d` timeframe.
3.  **Data Extraction:**
    * **Top Trends:** Queries with the highest overall search volume.
    * **Rising Trends:** Queries with the most significant growth in volume recently (useful for spotting "viral" topics).
4.  **Serialization:** Converts the resulting DataFrames into a JSON-friendly dictionary.

## 📝 Example Output

```json
{
    "keyword": "دانلود",
    "top_trends": [
        {"query": "دانلود آهنگ", "value": 100},
        {"query": "دانلود فیلم", "value": 85}
    ],
    "rising_trends": [
        {"query": "دانلود آهنگ جدید X", "value": 1250}
    ]
}
