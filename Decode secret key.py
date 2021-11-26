from stellar_sdk import Server, Keypair, TransactionBuilder, Network
import requests
key = input("Enter your Key: ")

print(Keypair.from_secret(key))
