#Based on MatejMecka's SQ205.py
#This is a Publicnet version
"""
Challenge 6: Claim 100 balances
Their will be 100 Balances in every account, you need to run this script 10x then submit the xdr in the wbsit (it will sign it) 
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Transaction, Network, FeeBumpTransaction, ClaimPredicate, Claimant, Asset
import requests

# 1. Load Keys
server = Server("https://horizon.stellar.org")
quest_account_pub_key = ("YOUR PUBLICKEY HERE")

# 2. Create Transaction
print("You can claim 10 Balances for every Sq")

base_fee = server.fetch_base_fee()
account = server.load_account(quest_account_pub_key)

# Claim Claimable Balance
balance_id = "" 
if len(balance_id) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id = balances["_embedded"]["records"][0]["id"]

balance_id2 = "" 
if len(balance_id2) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id2 = balances["_embedded"]["records"][1]["id"]

balance_id3 = "" 
if len(balance_id3) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id3 = balances["_embedded"]["records"][2]["id"]

balance_id4 = "" 
if len(balance_id4) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id4 = balances["_embedded"]["records"][3]["id"]

balance_id5 = "" 
if len(balance_id5) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id5 = balances["_embedded"]["records"][4]["id"]    

balance_id6 = "" 
if len(balance_id6) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id6 = balances["_embedded"]["records"][5]["id"]

balance_id7 = "" 
if len(balance_id7) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id7 = balances["_embedded"]["records"][6]["id"]

balance_id8 = "" 
if len(balance_id8) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id8 = balances["_embedded"]["records"][7]["id"]

balance_id9 = "" 
if len(balance_id9) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id9 = balances["_embedded"]["records"][8]["id"]

balance_id10 = "" 
if len(balance_id10) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id10 = balances["_embedded"]["records"][9]["id"]

print(f"Balance ID1: {balance_id}...")
print(f"Balance ID2: {balance_id2}...")
print(f"Balance ID3: {balance_id3}...")
print(f"Balance ID4: {balance_id4}...")
print(f"Balance ID5: {balance_id5}...")
print(f"Balance ID6: {balance_id6}...")
print(f"Balance ID7: {balance_id7}...")
print(f"Balance ID8: {balance_id8}...")
print(f"Balance ID9: {balance_id9}...")
print(f"Balance ID10: {balance_id10}...")

transaction = TransactionBuilder(
    source_account=account,
    network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE
).append_claim_claimable_balance_op(
    balance_id=balance_id,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id2,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id3,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id4,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id5,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id6,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id7,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id8,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id9,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id10,
    source=quest_account_pub_key
).build()

xdr = transaction.to_xdr()

print(f"Post this XDR @ SQ Xdr Box: {xdr}")
print(f"Check stellar.expert/explorer if all balances are gone, if all gone, merge using laboratory.stellar.org")
