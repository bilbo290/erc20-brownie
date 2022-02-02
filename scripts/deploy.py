from brownie import OurToken, network, config
from scripts.helpful_scripts import get_account, get_contract
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")
initial_supply_ether = Web3.fromWei(initial_supply, "ether")


def deploy():
    account = get_account()
    token = OurToken.deploy(initial_supply, {"from": account})
    print(f"{account} deployed {initial_supply_ether} TOAD")
    return token


def main():
    token = deploy()
