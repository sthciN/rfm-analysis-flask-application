from datetime import datetime

import numpy as np
import pandas as pd
import plotly.io as pio

from utils.helper import RFM_ERROR, CustomerNotFoundErr, ValueNotFoundErr

pio.templates.default = "plotly_white"

def rfm_score_analysis(customer_id):
    try:
        data= pd.read_csv("./data/rfm_dataset.csv")

    except FileNotFoundError as exc:
        raise FileNotFoundError from exc

    try:
        if data[data['CustomerID']==customer_id]['CustomerID'].empty:
            raise CustomerNotFoundErr

        elif 'RFM_Score' not in data.columns:
            raise RFM_ERROR

    except RFM_ERROR:
        data['PurchaseDate'] = pd.to_datetime(data['PurchaseDate'])

        # Add Recency
        data['Recency'] = (datetime.now().date() - data['PurchaseDate'].dt.date)/ np.timedelta64(1, 'D')
        data['Recency'] = data['Recency'].astype(int)

        # Add Frequency
        frequency_data = data.groupby('CustomerID')['OrderID'].count().reset_index()
        frequency_data.rename(columns={'OrderID': 'Frequency'}, inplace=True)
        data = data.merge(frequency_data, on='CustomerID', how='left')
        data['Frequency'] = data['Frequency'].astype(int)

        # Add Monetary
        monetary_data = data.groupby('CustomerID')['TransactionAmount'].sum().reset_index()
        monetary_data.rename(columns={'TransactionAmount': 'Monetary'}, inplace=True)
        data = data.merge(monetary_data, on='CustomerID', how='left')
        data['Monetary'] = data['Monetary'].astype(int)

        # Grouping RFM scores into 5
        recency_scores = [5, 4, 3, 2, 1]  # Higher to lower recency, less recent less higher
        frequency_scores = [1, 2, 3, 4, 5]  # Lower to higher frequency, more frequent more higher
        monetary_scores = [1, 2, 3, 4, 5]  # Lower to higher monetary, more monetary more higher

        data['RScore'] = pd.cut(data['Recency'], bins=5, labels=recency_scores)
        data['FScore'] = pd.cut(data['Frequency'], bins=5, labels=frequency_scores)
        data['MScore'] = pd.cut(data['Monetary'], bins=5, labels=monetary_scores)

        data['RScore'] = data['RScore'].astype(int)
        data['FScore'] = data['FScore'].astype(int)
        data['MScore'] = data['MScore'].astype(int)

        data['RFM_Score'] = data['RScore'] + data['FScore'] + data['MScore']
        data.to_csv("./data/rfm_dataset.csv", index=False)

    rfm_values = data[data['CustomerID']==customer_id]['RFM_Score']
    if not rfm_values.any():
        raise ValueNotFoundErr

    print('::::::::::::rfm_values', rfm_values)
    rfm = int(rfm_values.values[0])

    return rfm
