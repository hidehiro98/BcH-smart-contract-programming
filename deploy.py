from populus import Project
from populus.utils.wait import wait_for_transaction_receipt
from web3 import Web3

class Greeter:

    def __init__(self, account, passphrase):
        project = Project()
        chain_name = "bch"

        with project.get_chain(chain_name) as chain:
            GreeterFactory = chain.provider.get_contract_factory('Greeter')

            # 署名
            chain.web3.personal.unlockAccount(account, passphrase)

            # チェーンをdeploy
            txid = GreeterFactory.deploy(
                transaction={"from": account},
                args=[]
            )
            contract_address = chain.wait.for_contract_address(txid)
            self.account = account
            self.greeter = GreeterFactory(address = contract_address)
            self.chain = chain


    def setGreeting(self, greeting):
        txid = self.greeter.transact(
            transaction={"from": self.account}
        ).setGreeting(greeting)
        self.chain.wait.for_receipt(txid)


    def greet(self):
        return self.greeter.call().greet()


if __name__ == '__main__':

    # simple test code and usage
    a = Greeter('0x857b97371202791b18d415179c0fbfe16d28802d', 'password')

    print(a.greet())
    a.setGreeting('How are you?')
    print(a.greet())


# end of deploy.py
