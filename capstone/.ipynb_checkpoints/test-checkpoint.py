{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "41d9c1ed",
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
    "import duckdb\n",
    "import streamlit as st\n",
    "from gsheetsdb import connect"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a30e2774",
   "metadata": {},
   "outputs": [
    {
     "ename": "TomlDecodeError",
     "evalue": "Found tokens after a closed string. Invalid TOML. (line 1 column 1 char 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\toml\\decoder.py\u001b[0m in \u001b[0;36mloads\u001b[1;34m(s, _dict, decoder)\u001b[0m\n\u001b[0;32m    510\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 511\u001b[1;33m                 ret = decoder.load_line(line, currentlevel, multikey,\n\u001b[0m\u001b[0;32m    512\u001b[0m                                         multibackslash)\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\toml\\decoder.py\u001b[0m in \u001b[0;36mload_line\u001b[1;34m(self, line, currentlevel, multikey, multibackslash)\u001b[0m\n\u001b[0;32m    777\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 778\u001b[1;33m             \u001b[0mvalue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvtype\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mload_value\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpair\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstrictly_valid\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    779\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\toml\\decoder.py\u001b[0m in \u001b[0;36mload_value\u001b[1;34m(self, v, strictly_valid)\u001b[0m\n\u001b[0;32m    848\u001b[0m                         \u001b[1;32mif\u001b[0m \u001b[0mclosed\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 849\u001b[1;33m                             raise ValueError(\"Found tokens after a closed \" +\n\u001b[0m\u001b[0;32m    850\u001b[0m                                              \"string. Invalid TOML.\")\n",
      "\u001b[1;31mValueError\u001b[0m: Found tokens after a closed string. Invalid TOML.",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mTomlDecodeError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-12-2aa63e89567b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0msheet_url\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mst\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msecrets\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"public_gsheets_url\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msheet_url\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\secrets.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    150\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    151\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__getitem__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 152\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    153\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    154\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__repr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\secrets.py\u001b[0m in \u001b[0;36m_parse\u001b[1;34m(self, print_exceptions)\u001b[0m\n\u001b[0;32m     95\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     96\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 97\u001b[1;33m                 \u001b[0msecrets\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtoml\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mloads\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msecrets_file_str\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     98\u001b[0m             \u001b[1;32mexcept\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     99\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[0mprint_exceptions\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\toml\\decoder.py\u001b[0m in \u001b[0;36mloads\u001b[1;34m(s, _dict, decoder)\u001b[0m\n\u001b[0;32m    512\u001b[0m                                         multibackslash)\n\u001b[0;32m    513\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mValueError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 514\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mTomlDecodeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0merr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moriginal\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpos\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    515\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mret\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    516\u001b[0m                 \u001b[0mmultikey\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmultilinestr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmultibackslash\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mret\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTomlDecodeError\u001b[0m: Found tokens after a closed string. Invalid TOML. (line 1 column 1 char 0)"
     ]
    }
   ],
   "source": [
    "sheet_url = st.secrets[\"public_gsheets_url\"]\n",
    "print(sheet_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0ab410f5",
   "metadata": {},
   "outputs": [
    {
     "ename": "TomlDecodeError",
     "evalue": "Found tokens after a closed string. Invalid TOML. (line 1 column 1 char 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\toml\\decoder.py\u001b[0m in \u001b[0;36mloads\u001b[1;34m(s, _dict, decoder)\u001b[0m\n\u001b[0;32m    510\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 511\u001b[1;33m                 ret = decoder.load_line(line, currentlevel, multikey,\n\u001b[0m\u001b[0;32m    512\u001b[0m                                         multibackslash)\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\toml\\decoder.py\u001b[0m in \u001b[0;36mload_line\u001b[1;34m(self, line, currentlevel, multikey, multibackslash)\u001b[0m\n\u001b[0;32m    777\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 778\u001b[1;33m             \u001b[0mvalue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvtype\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mload_value\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpair\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstrictly_valid\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    779\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\toml\\decoder.py\u001b[0m in \u001b[0;36mload_value\u001b[1;34m(self, v, strictly_valid)\u001b[0m\n\u001b[0;32m    848\u001b[0m                         \u001b[1;32mif\u001b[0m \u001b[0mclosed\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 849\u001b[1;33m                             raise ValueError(\"Found tokens after a closed \" +\n\u001b[0m\u001b[0;32m    850\u001b[0m                                              \"string. Invalid TOML.\")\n",
      "\u001b[1;31mValueError\u001b[0m: Found tokens after a closed string. Invalid TOML.",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mTomlDecodeError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-11-ceb1e4c2e4d2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      9\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mrows\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m \u001b[0msheet_url\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mst\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msecrets\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"public_gsheets_url\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     12\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msheet_url\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\secrets.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    150\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    151\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__getitem__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 152\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    153\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    154\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__repr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\secrets.py\u001b[0m in \u001b[0;36m_parse\u001b[1;34m(self, print_exceptions)\u001b[0m\n\u001b[0;32m     95\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     96\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 97\u001b[1;33m                 \u001b[0msecrets\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtoml\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mloads\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msecrets_file_str\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     98\u001b[0m             \u001b[1;32mexcept\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     99\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[0mprint_exceptions\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\toml\\decoder.py\u001b[0m in \u001b[0;36mloads\u001b[1;34m(s, _dict, decoder)\u001b[0m\n\u001b[0;32m    512\u001b[0m                                         multibackslash)\n\u001b[0;32m    513\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mValueError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 514\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mTomlDecodeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0merr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moriginal\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpos\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    515\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mret\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    516\u001b[0m                 \u001b[0mmultikey\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmultilinestr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmultibackslash\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mret\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTomlDecodeError\u001b[0m: Found tokens after a closed string. Invalid TOML. (line 1 column 1 char 0)"
     ]
    }
   ],
   "source": [
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
    "print(sheet_url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8b487b1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5678e805",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c7d8887",
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
