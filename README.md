# RFM Analysis
Utilized for comprehending and categorizing customers according to their purchasing patterns, RFM Analysis relies on three crucial metrics: recency, frequency, and monetary value. These metrics offer insights into customer engagement, loyalty, and their value to a business. If you're interested in learning how to conduct RFM Analysis, this article is tailored for you. Within this piece, I will guide you through the process of performing RFM Analysis using Python.

Through RFM Analysis, a company can evaluate customers based on:

Recency: the date of their most recent purchase
Frequency: how often they make purchases
Monetary value: the amount spent on purchases

## Requirements
To conduct RFM analysis with Python, it's essential to have a dataset containing customer IDs, purchase dates, and transaction amounts. With this data, we can compute RFM values for individual customers, allowing us to analyze their purchasing patterns and behaviors. I have identified a suitable dataset for this purpose, and you can access and download it [here](https://www.kaggle.com/datasets/harshsingh2209/rfm-analysis).
After downloading the dataset, move it to the `data` folder.
Find the API_KEY configuration withing the `.env` file.

## Code Structure
```
├── README.md
├── app
│   └── __init__.py
├── controller
├── data
├── main.py
├── requirements.txt
├── rfm_score.py
├── utils
│   ├── auth.py
│   ├── constants.py
│   ├── helper.py
│   └── routes.py
```

## How to Run
To run the application use: `python main.py`. 

This application will read the csv file in the data directory and enrich it after calculating the recensy, frequency, monatary and RFM scores. By requesting to the main route of this application with this address:

```
/rfm-score/<customer_id>
```

you will find the regarded RFM score.

Request example:

```
GET /rfm-score/8317
headers {"Authorization": "an-api-key"}
```

Response example:
```
{
  "result": {
    "rfm_score": 7
  }
}
```
