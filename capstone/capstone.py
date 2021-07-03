import requests #-> Để gọi API
import re #-> Để xử lý data dạng string
from datetime import datetime as dt #-> Để xử lý data dạng datetime
import gspread #-> Để update data lên Google Spreadsheet
from gspread_dataframe import set_with_dataframe #-> Để update data lên Google Spreadsheet
import pandas as pd #-> Để update data dạng bản
pd.plotting.register_matplotlib_converters()
import json 
from google.oauth2 import service_account #-> Để nhập Google Spreadsheet Credentials
import os
import matplotlib.pyplot as plt
import seaborn as sns
import duckdb
import streamlit as st
from gsheetsdb import connect

dataframe = pd.read_csv(r'C:\Users\gtp43728\OneDrive - GSK\Documents\GitHub\atom-assignments\capstone\sale2019\sales2019_3.csv')
dataframe.head()