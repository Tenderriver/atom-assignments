{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "118af876",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests #-> Để gọi API\n",
    "import re #-> Để xử lý data dạng string\n",
    "from datetime import datetime as dt #-> Để xử lý data dạng datetime\n",
    "import gspread #-> Để update data lên Google Spreadsheet\n",
    "from gspread_dataframe import set_with_dataframe #-> Để update data lên Google Spreadsheet\n",
    "import pandas as pd #-> Để update data dạng bản\n",
    "pd.plotting.register_matplotlib_converters()\n",
    "import json \n",
    "from oauth2client.service_account import ServiceAccountCredentials #-> Để nhập Google Spreadsheet Credentials\n",
    "import os\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import seaborn as sns\n",
    "import duckdb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4855ad33",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-7d4daefe20d7>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mgsheetsdb\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mconnect\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;31m# Create a connection object.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mconn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from gsheetsdb import connect\n",
    "\n",
    "# Create a connection object.\n",
    "conn = connect()\n",
    "\n",
    "# Perform SQL query on the Google Sheet.\n",
    "# Uses st.cache to only rerun when the query changes or after 10 min.\n",
    "@st.cache(ttl=600)\n",
    "def run_query(query):\n",
    "    rows = conn.execute(query, headers=1)\n",
    "    return rows\n",
    "\n",
    "sheet_url = st.secrets[\"public_gsheets_url\"]\n",
    "rows = run_query(f'SELECT * FROM \"{sheet_url}\"')\n",
    "\n",
    "# Print results.\n",
    "for row in rows:\n",
    "    st.write(f\"{row.name} has a :{row.pet}:\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c34cc7a8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
