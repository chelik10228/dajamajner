import random;
import time;
import os;

print("======================================");
print("Dajamajner");
print("======================================");
currency = input("Enter currency: ");
time.sleep(1);
with open("wallet.txt", "w") as f:
				print();

while (True):
	money = random.uniform(0, 1000);
	hex_string = hex(int(money));
	with open("wallet.txt", "a") as f:

				print((hex_string), "|", money, currency+"s", "\n", file=f);

	print("======================================");
	print("\033[33mWallet name: Wallet.Wal\033[0m");
	print("Wallet size: ", os.path.getsize('wallet.txt'));
	print("\033[32mGiven:", money, currency, "\033[0m");
  
