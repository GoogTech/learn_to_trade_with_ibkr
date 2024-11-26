import requests
import urllib3
import json
from typing import *

# Author: HackHuang
# Description: Learn to trade with IBKR’s Client Portal API 
# Last Modified Date: 2024/11/25

# /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/urllib3/connectionpool.py:1099: 
# InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. 
# Adding certificate verification is strongly advised. 
# See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warningswarnings.warn(
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_RUL: Final = 'https://localhost:8888/v1/api/'
LOGIN_STATUS_ENDPOINT: Final = 'iserver/auth/status'
SEARCH_ENDPOINT: Final = 'iserver/secdef/search'
INFO_ENDPOINT: Final = 'iserver/secdef/info'

def check_login_status() -> None:
    """Check the login status
    Lesson 2: https://www.interactivebrokers.com/campus/trading-lessons/launching-and-authenticating-the-gateway/
    """
    auth_response = requests.get(url=BASE_RUL + LOGIN_STATUS_ENDPOINT, verify=False)
    print(f'auth_response: {auth_response}')
    print(f'auth_response.text: {auth_response.text}')

def search_contract() -> None:
    """Lesson 3: search contract by symbol and secType
    https://www.interactivebrokers.com/campus/trading-lessons/contract-search/
    """
    # 1.The 'symbol' is the trade code, such as Apple's stock code is APPL,
    # but it's note that TSLA(NASDAQ) means the Tsla stock in NASDAQ.
    # 2.The 'secType' is the type of trade tool, such as STK represent the trade type is stock,
    # and the ETF represent the type of trade tool is Exchange-Traded Fund.
    # 3.The field 'name' can be used to search for a company name instead of just the standard symbol.
    post_json = {'symbol': 'Tsla', 'secType': 'STK', 'name': False}
    contract_response = requests.post(url=BASE_RUL + SEARCH_ENDPOINT, json=post_json, verify=False)
    contract_response_json = json.dumps(obj=contract_response.json(), indent=2)
    print(contract_response_json)

def get_contract_info() -> None:
    """Get contract info by conid ect...
    Lesson 3: https://www.interactivebrokers.com/campus/trading-lessons/contract-search/
    """
    # 1.conid: Each security(证劵), option(期权), future(期货), bond(债券), 
    # and other financial instrument(金融工具) is assigned a unique conid.
    # 2.exchange: Exchange represents the trading exchange(交易所) or market of a security.
    conid: str = 'conid=76792991'
    sec_type: str = 'secType=STK'
    month: str = 'month=JUL24'
    exchange: str = 'exchange=NASDAQ'
    # strike = 'strike=580'
    # right = 'right=C'
    # request_params: str = '&'.join([conid, sec_type, month, exchange, strike, right])
    request_params: str = '&'.join([conid, sec_type, month, exchange])
    request_url: str = ''.join([BASE_RUL, INFO_ENDPOINT, '?', request_params])
    response: requests.models.Response = requests.get(url=request_url, verify=False)
    response_json: str = json.dumps(response.json(), indent=2)
    print(response_json)

# check_login_status()
# search_contract()
# get_contract_info()