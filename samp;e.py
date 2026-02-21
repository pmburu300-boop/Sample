from dataclasses import dataclass
from datetime import datetime


# -----------------------------
# Models
# -----------------------------

@dataclass
class Customer:
    customer_id: int
    name: str
    address: str
    previous_reading: float = 0.0


@dataclass
class Bill:
    customer_id: int
    usage: float
    rate: float
    total_amount: float
    date: str


# -----------------------------
# Billing Logic
# -----------------------------

RATE_PER_CUBIC_METER = 2.5  # example rate


def calculate_usage(previous: float, current: float) -> float:
    if current < previous:
        raise ValueError("Current reading cannot be less than previous reading.")
    return current - previous


def calculate_bill_amount(usage: float, rate: float) -> float:
    return usage * rate


# -----------------------------
# In-Memory Storage
# -----------------------------

customers = {}
bills = []


# -----------------------------
# Service Functions
# -----------------------------

def add_customer():
    customer_id = int(input("Enter customer ID: "))
    name = input("Enter customer name: ")
    address = input("Enter address: ")

    if customer_id in customers:
        print("Customer ID already exists!")
        return

    customer = Customer(customer_id, name, address)
    customers[customer_id] = customer
    print("Customer added successfully.\n")


def view_customers():
    if not customers:
        print("No customers found.\n")
        return

    for customer in customers.values():
        print(customer)
    print()


def add_meter_reading():
    customer_id = int(input("Enter customer ID: "))

    if customer_id not in customers:
        print("Customer not found.\n")
        return

    customer = customers[customer_id]
    current_reading = float(input("Enter current meter reading: "))

    try:
        usage = calculate_usage(customer.previous_reading, current_reading)
        total = calculate_bill_amount(usage, RATE_PER_CUBIC_METER)

        bill = Bill(
            customer_id=customer_id,
            usage=usage,
            rate=RATE_PER_CUBIC_METER,
            total_amount=total,
            date=str(datetime.now())
        )

        bills.append(bill)

        # Update previous reading
        customer.previous_reading = current_reading

        print("\nBill Generated:")
        print(bill)
        print()

    except ValueError as e:
        print("Error:", e)
        print()


def view_bills():
    if not bills:
        print("No bills generated.\n")
        return

    for bill in bills:
        print(bill)
    print()


# -----------------------------
# Menu System
# -----------------------------

def main_menu():
    while True:
        print("====== Water Billing System ======")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Add Meter Reading & Generate Bill")
        print("4. View Bills")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            add_meter_reading()
        elif choice == "4":
            view_bills()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.\n")


# -----------------------------
# Entry Point
# -----------------------------

if __name__ == "__main__":
    main_menu()