from decimal import Decimal, InvalidOperation


class ATM:
	def __init__(self, balance: Decimal = Decimal("1000.00"), pin: str = "1234") -> None:
		self.balance = balance
		self.pin = pin

	def run(self) -> None:
		print("Welcome to the ATM")
		if not self._authenticate():
			print("Too many incorrect PIN attempts. Your session has ended.")
			return

		while True:
			print("\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
			choice = input("Choose an option: ").strip()

			if choice == "1":
				print(f"Current balance: ${self.balance:.2f}")
			elif choice == "2":
				self._deposit()
			elif choice == "3":
				self._withdraw()
			elif choice == "4":
				print("Thank you for using the ATM.")
				return
			else:
				print("Invalid option. Choose 1, 2, 3, or 4.")

	def _authenticate(self) -> bool:
		for _ in range(3):
			if input("Enter your 4-digit PIN: ").strip() == self.pin:
				return True
			print("Incorrect PIN.")
		return False

	@staticmethod
	def _read_amount() -> Decimal | None:
		try:
			amount = Decimal(input("Enter amount: ").strip())
		except InvalidOperation:
			print("Enter a valid amount.")
			return None

		if not amount.is_finite() or amount <= 0 or amount != amount.quantize(Decimal("0.01")):
			print("Amount must be positive and no more than two decimal places.")
			return None
		return amount

	def _deposit(self) -> None:
		amount = self._read_amount()
		if amount is not None:
			self.balance += amount
			print(f"Deposit successful. New balance: ${self.balance:.2f}")

	def _withdraw(self) -> None:
		amount = self._read_amount()
		if amount is None:
			return
		if amount > self.balance:
			print("Insufficient funds.")
			return
		self.balance -= amount
		print(f"Withdrawal successful. New balance: ${self.balance:.2f}")


if __name__ == "__main__":
	ATM().run()
