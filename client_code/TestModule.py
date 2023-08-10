from anvil.js import import_from
from anvil.js import window

# or instead of using "ethers" as defined in the importmap use:
# "https://cdnjs.cloudflare.com/ajax/libs/ethers/6.6.0/ethers.min.js"
print(window.__dir__())
web3auth = import_from("@web3auth/modal")
print(web3auth)