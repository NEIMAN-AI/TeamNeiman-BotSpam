import sys
import glob
import asyncio
import logging
import importlib
import urllib3


from pathlib import Path
from config import N1, N2, N3, N4, N5, N6, N7, N8, N9, N10


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_plugins(plugin_name):
    path = Path(f"NeimanBot/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"NeimanBot.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["NeimanBot.modules." + plugin_name] = load
    print("Neiman has Imported " + plugin_name)


files = glob.glob("NeimanBot/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\n⚡𝐍𝐞𝐢𝐦𝐚𝐧𝐁𝐨𝐭 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ⚡\nMy Master ---> @NeimanBoy_OP")


async def main():
    await N1.run_until_disconnected()
    await N2.run_until_disconnected()
    await N3.run_until_disconnected()
    await N4.run_until_disconnected()
    await N5.run_until_disconnected()
    await N6.run_until_disconnected()
    await N7.run_until_disconnected()
    await N8.run_until_disconnected()
    await N9.run_until_disconnected()
    await N10.run_until_disconnected()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
