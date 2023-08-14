from anvil import js
from .utils import _component_helpers as helpers

_root = "https://cdn.jsdelivr.net/npm/@web3auth"
_modules = ["modal", "metamask-adapter", "coinbase-adapter"]
_version = "6.1.7"
_default_config = {
    "clientId": "BIKwLAaWOBYuG9hFEmiGUtUciRC09VX6DECnOlmtqZDjpaih_bhTE3atOpx3tgTDeeVbEBAFg3VN23j7crRfpn8",
    "chainConfig": {
        "chainNamespace": "eip155",
        "chainId": "0x5",
        "rpcTarget": "https://rpc.ankr.com/eth",
    },
}


def _kebab_to_pascal(kebab):
    camel = "".join(x.capitalize() for x in kebab.lower().split("-"))
    return kebab[0].lower() + camel[1:]


for module in _modules:
    url = f"{_root}/{module}@{_version}/dist/{_kebab_to_pascal(module)}.umd.min.js"
    helpers._html_injector.cdn(url)


def login_with_web3auth(config=None):
    config = config or _default_config
    metamask_adapter = js.window.MetamaskAdapter.MetamaskAdapter()
    coinbase_adapter = js.window.CoinbaseAdapter.CoinbaseAdapter()
    web3auth = js.window.Modal.Web3Auth(config)
    web3auth.configureAdapter(metamask_adapter)
    web3auth.configureAdapter(coinbase_adapter)
    web3auth.initModal()
    web3auth.connect()
