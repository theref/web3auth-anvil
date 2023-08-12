from anvil import js


web3auth_config = {
    "clientId": "BIKwLAaWOBYuG9hFEmiGUtUciRC09VX6DECnOlmtqZDjpaih_bhTE3atOpx3tgTDeeVbEBAFg3VN23j7crRfpn8",
    "chainConfig": {
        "chainNamespace": "eip155",
        "chainId": "0x5",
        "rpcTarget": "https://rpc.ankr.com/eth",
    },
}
metamask_adapter = js.window.MetamaskAdapter.MetamaskAdapter()
coinbase_adapter = js.window.CoinbaseAdapter.CoinbaseAdapter()
web3auth = js.window.Modal.Web3Auth(web3auth_config)
web3auth.configureAdapter(metamask_adapter)
web3auth.configureAdapter(coinbase_adapter)
web3auth.initModal()
web3auth.connect()