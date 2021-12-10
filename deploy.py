import os
import dotenv
from pathlib import Path
import solcx
import json
from web3 import Web3
from solcx import compile_standard, install_solc


solcx.install_solc("0.6.0")

from dotenv import load_dotenv

load_dotenv()


with open("./simpleStorage.sol", "r") as file:

    simple_storage_file = file.read()


# compiling our solidity, this will be equal to calling our compile_standard function, but with variables and perameters to the function
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.0",
)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)


bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]
# what we are doing here is we are walking down the json, so we are in the compiled_sol json, we are going to contracts,
# SimpleStorage.sol, SimpleStorage, evm, and then getting the bytecode object, the bytecode of our contract
# the bytecode of our contract is the low level stuff that the ethereum virtual machine(evm) will understand

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
# if we then look in the json file, we see that in the abi is all of our functions, and so abi is the object that contains all of our function.

# for connecting to ganache(if we were connecting to metamask etc we would use the metamask link)
w3 = Web3(Web3.HTTPProvider("HTTP://0.0.0.0:7545"))
chain_id = 1337  # is found in ganache
my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"  # any address we want to deploy the contract from
private_key = os.getenv("PRIVATE_KEY")
# the private key we need to make transactions
print(os.getenv("PRIVATE_KEY"))

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# we need to build a transaction, sign a transaction then send a transaction
# get latest transaction
nonce = w3.eth.getTransactionCount(my_address)

# build a transaction
# sign a transaction
# send a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
        "gasPrice": w3.eth.gas_price,
    }
)
singed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# signed_txn is signing a contract that is deploying to the blockchain that anyone can verify
print("Deploying Contract...")

# environment variables are variables that we can set in our terminal and command lines
# export PRIVATE_KEY=0xaa312477040f2296640823b37e1aab1422114df0effb922b818f608866eb9f2e
# then when we type echo $PRIVATE_KEY - the terminal will show the variable PRIVAT_KEY that was entered into the terminal
# not when we close our shell this variable will be lost and would have to be reinputted
# we can then access this environment variable when we enter os.getenv("variable"), we just first have to have import os at the top

# send a transaction to the blockchain
txn_hash = w3.eth.send_raw_transaction(singed_txn.rawTransaction)
# waiting for soem block confirmations to happen, this will have our code stop and wait for the txn_has to go through
txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
print("Deployed!")
# working with the contract, you always need
# Contract Address
# Contract ABI
simple_storage = w3.eth.contract(address=txn_receipt.contractAddress, abi=abi)
# now that we have the contract address and abi, we can start interacting with it.
# When making transactions on the blockchains there are two ways in which we can interact with them -
# Call -> Simulate making the call and getting a return value, dont make a state change to the blockchain, we can call 'non-view' functions and not make a state change
# Transact -> actually make a state change to the blockchain
# note, when you transact on a view function it will not make a state change as the function itself does not make a state change.

# This is our inital value of our store number, because if we go into our simpleStorage file we have the retrieve function which returns the favorite number
print(
    simple_storage.functions.retrieve().call()
)  # the .call() here is us interacting using a call.
print("Updating Contract...")
store_transaction = simple_storage.functions.store(81).buildTransaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce + 1,
        "gasPrice": w3.eth.gas_price,
        # Here we are adding in all of our previous data which we had in the previous buildTransaction.
        # we are also adding one to our nonce since a nonce can only be used once
    }
)
signed_store_tx = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
send_store_txn = w3.eth.send_raw_transaction(signed_store_tx.rawTransaction)
tx_reciept = w3.eth.wait_for_transaction_receipt(send_store_txn)
print(
    "Contract Updated!"
)  # By adding in these prompts, we allow ourselves and users to understand what is going on, what we are waiting for etc
