import pandas as pd
import streamlit as st
import requests
from PIL import Image


SECRET  = "205eaa221fb98013ea670bb95654a81d"

URL = "https://eth-mainnet.gateway.pokt.network/v1/lb/618e0ab63853830035c9617b"
HDR = {
	"Content-Type": "application/json",
	"user": SECRET
}

def use(method, params=[]):
    '''To call a method using the Pocket API'''
    DAT = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }
    r = requests.post(URL, headers=HDR, json=DAT)
    print(method, ":", r.status_code, r.reason)
    return r.json()
    

image = Image.open('pokt.png')

st.image(image)

st.title("Ethereum Transaction details")

tnx_hash = None

while tnx_hash==None:
	tnx_hash = st.text_input('Enter transaction hash (starting with 0x)')



result_json = use("eth_getTransactionByHash", [str(tnx_hash)])["result"]
block_number_hex = result_json["blockNumber"]
block_hash = result_json["blockHash"]
sender_address = result_json["from"]
receiver_address = result_json["to"]
gas_hex = result_json["gas"]
gas_price_hex = result_json["gasPrice"]
nonce_hex = result_json["nonce"]
transaction_index_hex = result_json["transactionIndex"]
value_hex = result_json["value"]


block_number = int(str(block_number_hex), base=16)
gas = int(str(gas_hex), base=16)
gas_price = int(str(gas_price_hex), base=16)
nonce = int(str(nonce_hex), base=16)
transaction_index = int(str(transaction_index_hex), base=16)
value = int(str(value_hex), base=16)

#st.metric(label="Block Number", value=block_number)
#st.write(block_hash)
#st.write(sender_address)
#st.write(receiver_address)
#st.write(gas)
#st.write(gas_price)
#st.write(nonce)
#st.write(transaction_index)
#st.write(value)


col1, col2, col3 = st.columns(3)
col1.metric("Block Number", block_number)
col2.metric("Gas Limit", gas)
col3.metric("Gas Price (Gwei)", round(float(gas_price/10**9),2))
col1, col2, col3 = st.columns(3)
col1.metric("Value (Ether)", round(float(value/10**16),2))
col2.metric("Nonce", nonce)
col3.metric("Transaction Index", transaction_index)
col1, col2, col3 = st.columns(3)
col1.metric("Block Hash", block_hash)
col2.metric("Sender Address", sender_address)
col3.metric("Receiver Address", receiver_address)

#st.metric(label="Gas price", value=4, delta=-0.5,delta_color="inverse")
#st.metric(label="Active developers", value=123, delta=123,delta_color="off")
