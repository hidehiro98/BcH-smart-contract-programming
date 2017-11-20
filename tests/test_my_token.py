import pytest

# pre action of the tests,
@pytest.fixture()
def token_contract(chain):
    TokenFactory = chain.provider.get_contract_factory('MyToken')

    # 0 is initial balance, BcH is name, BcH is unit, 0 is underflow
    deploy_txid = TokenFactory.deploy(args=[
        0,
        "BcH Coin",
        "BcH",
        0,
    ])

    contract_address = chain.wait.for_contract_address(deploy_txid)

    return TokenFactory(address=contract_address)

# token_contract is the first method token_contract?
def test_my_token(token_contract, chain):

    # web3 is Ethereum library, 10 accounts are already prepared by populus pytest function
    account0 = chain.web3.eth.accounts[0]
    account1 = chain.web3.eth.accounts[9]

    # we can modify who call the method, by using .call()
    assert token_contract.call().getBalanceOf(account0) == 1000000
    assert token_contract.call().getBalanceOf(account1) == 0

    txid = token_contract.transact().transfer(account1, 10)

    # with "--capture=no" option, we can see the result by print
    print(token_contract, len(chain.web3.eth.accounts))

    # we need to wait to write it in chain
    chain.wait.for_receipt(txid)

    assert token_contract.call().getBalanceOf(account0) == 999990
    assert token_contract.call().getBalanceOf(account1) == 10

# end of test_my_token.py
