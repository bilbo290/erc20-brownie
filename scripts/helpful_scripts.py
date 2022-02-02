from brownie import network, config, accounts, OurToken, Contract
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]

    if id:
        return accounts.load(id)

    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]

    return accounts.add(config["wallets"]["from_key"])


contract_to_mock = {
    "token_contract": OurToken,
}


def get_contract(contract_name):
    """This function will grab the contract addresses from the brownie config if defined, otherwise,
    it will deploy a mock version of that contract, and return that mock contract.

        Args:
            contract_name (string): This is the name that is referred to in the
            brownie config and 'contract_to_mock' variable.
        Returns:
            brownie.network.contract.ProjectContract: The most recently deployed
            Contract of the type specificed by the dictionary. This could be either
            a mock or the 'real' contract on a live network.
    """
    initial = 1000
    contract_type = contract_to_mock[contract_name]
    account = get_account()

    if len(contract_type) <= 0:
        # MockV3Aggregator.length
        print("No token deployed yet")
        print("Deploying Token")
        token = OurToken.deploy(initial, {"from": account})

        # MockV3Aggregator[-1], grab most recent mock contract
    else:
        token = contract_type[-1]
        token = Contract.from_abi(
            contract_type._name,
            "0x9F31210DD592F87C08F065043236BF57BD2CCC19",
            contract_type.abi,
        )
        print("Existing Token Deployed")
        # MockV3Aggregator.abi
    return token
