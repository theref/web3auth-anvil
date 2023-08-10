from ._anvil_designer import Form1Template
from anvil.js import window

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        # print(window.__dir__())
        # self.init_components(**properties)
        # web3auth_config = {
        #     "clientId": "YOUR_WEB3AUTH_CLIENT_ID",
        #     "chainConfig": {
        #         "chainNamespace": "eip155",
        #         "chainId": "0x5",
        #         "rpcTarget": "https://rpc.ankr.com/eth",
        #     },
        # }
        # web3auth = Web3Auth(web3auth_config)
        # web3auth.initModal()
        from ..TestModule import web3auth
