import asyncio
import logging
from v4_client_py.chain.aerial.wallet import LocalWallet
from v4_client_py.clients.dydx_subaccount import Subaccount

from v4_client_py.clients.dydx_validator_client import ValidatorClient
from v4_client_py.clients.constants import BECH32_PREFIX, Network

from tests.constants import DYDX_TEST_MNEMONIC


async def main() -> None:
    network = Network.staging()
    client = ValidatorClient(network.validator_config)
    wallet = LocalWallet.from_mnemonic(DYDX_TEST_MNEMONIC, BECH32_PREFIX);
    subaccount = Subaccount(wallet, 0)
    try:
        tx = client.post.withdraw(
            subaccount,
            0,
            10_000_000,
        )
        print('**Withdraw Tx**')
        print(tx)
    except Exception as e:
        print(e)

    

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
