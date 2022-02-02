from brownie import OurToken, network, config, Contract
from scripts.helpful_scripts import get_account


def checkBalance():
    token_address = config["networks"]["golden_toad"][
        "address"
    ]  ## GOLDEN TOAD CONTRACT ADDRESS
    contract = Contract.from_abi(OurToken._name, token_address, OurToken.abi)
    account = get_account()
    balance = contract.balanceOf(account)
    print(f"{account} now have {balance} toad")


def main():
    checkBalance()
