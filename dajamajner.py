import random;
import time;
import os;

print("======================================");
print("Dajamajner");
print("======================================");
time.sleep(1);
with open("wallet.wal.txt", "w") as f:
				print();

while (True):
	money = random.uniform(0, 1000);
	hex_string = hex(int(money));
	with open("wallet.wal.txt", "a") as f:

				print((hex_string), "|", money, "bitfols", "\n", file=f);

	print("======================================");
	print("\033[33mWallet name: Wallet.Wal\033[0m");
	print("Wallet size: ", os.path.getsize('wallet.wal.txt'));
	print("\033[32mGiven:", money, "bitfols", "\033[0m");
  
