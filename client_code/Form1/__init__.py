from ._anvil_designer import Form1Template
from anvil.js import window

class Form1(Form1Template):
    def __init__(self, **properties):
        web3auth_config = {
            "clientId": "BIKwLAaWOBYuG9hFEmiGUtUciRC09VX6DECnOlmtqZDjpaih_bhTE3atOpx3tgTDeeVbEBAFg3VN23j7crRfpn8",
            "chainConfig": {
                "chainNamespace": "eip155",
                "chainId": "0x5",
                "rpcTarget": "https://rpc.ankr.com/eth",
            },
        }
        metamask_adapter = window.MetamaskAdapter.MetamaskAdapter()
        coinbase_adapter = window.CoinbaseAdapter.CoinbaseAdapter()
        web3auth = window.Modal.Web3Auth(web3auth_config)
        web3auth.configureAdapter(metamask_adapter)
        web3auth.configureAdapter(coinbase_adapter)
        web3auth.initModal()
        web3auth.connect()
