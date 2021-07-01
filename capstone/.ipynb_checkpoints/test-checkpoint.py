{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6c288ee9",
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
   "execution_count": null,
   "id": "750d0bda",
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
