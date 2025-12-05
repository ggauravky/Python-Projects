"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400
  Neha owes ₹400
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""


def get_integer(prompt, min_value=1):
    while True:
        try:
            value = int(input(prompt).strip())
            if value < min_value:
                print(f"❌ Please enter a number greater than or equal to {min_value}.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid integer number.")


def get_float(prompt, min_value=0.01):
    while True:
        try:
            value = float(input(prompt).strip())
            if value < min_value:
                print(f"❌ Please enter an amount greater than ₹{min_value}.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number.")


def get_name(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name.title()  
        print("❌ Name cannot be empty. Please try again.")


def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        print("❌ Please enter 'y' for yes or 'n' for no.")


def print_header():
    print("\n" + "=" * 60)
    print("💰 BILL SPLITTER PRO 💰".center(60))
    print("=" * 60)


def print_summary_box(names, total_bill, tip_amount, grand_total, share_per_person):
    box_width = 60

    print("\n" + "╔" + "=" * (box_width - 2) + "╗")
    print("║" + " BILL SUMMARY ".center(box_width - 2) + "║")
    print("╠" + "=" * (box_width - 2) + "╣")

    print("║" + f" 👥 Total People: {len(names)}".ljust(box_width - 2) + "║")
    print("║" + f" 📝 Names: {', '.join(names)}".ljust(box_width - 2) + "║")
    print("╠" + "-" * (box_width - 2) + "╣")

    print(
        "║" + f" 🧾 Subtotal:        ₹{total_bill:>10,.2f}".ljust(box_width - 2) + "║"
    )
    if tip_amount > 0:
        tip_percentage = (tip_amount / total_bill) * 100
        print(
            "║"
            + f" 💵 Tip ({tip_percentage:.0f}%):        ₹{tip_amount:>10,.2f}".ljust(
                box_width - 2
            )
            + "║"
        )
    print(
        "║" + f" 💰 Grand Total:     ₹{grand_total:>10,.2f}".ljust(box_width - 2) + "║"
    )
    print("╠" + "=" * (box_width - 2) + "╣")

    print(
        "║"
        + f" 🎯 Each Person Pays: ₹{share_per_person:>10,.2f}".ljust(box_width - 2)
        + "║"
    )
    print("╠" + "=" * (box_width - 2) + "╣")

    for i, name in enumerate(names, 1):
        print(
            "║"
            + f"  {i}. {name:<20} ₹{share_per_person:>10,.2f}".ljust(box_width - 2)
            + "║"
        )

    print("╚" + "=" * (box_width - 2) + "╝")

    if len(names) > 1:
        total_paid = share_per_person * len(names)
        difference = round(grand_total - total_paid, 2)
        if abs(difference) > 0.01:
            print(
                f"\n⚠️  Note: Due to rounding, there's a ₹{abs(difference):.2f} difference."
            )
            print(f"   The last person can adjust by ₹{abs(difference):.2f}.")


def main():
    print_header()

    num_people = get_integer("\n👥 How many people are in the group? ", min_value=2)

    names = []
    print(f"\n📝 Let's get everyone's names:")
    for i in range(num_people):
        name = get_name(f"   Enter name of person {i + 1}: ")
        names.append(name)

    total_bill = get_float(f"\n🧾 Enter the total bill amount: ₹")

    tip_amount = 0
    if get_yes_no("\n💵 Would you like to add a tip? (y/n): "):
        tip_choice = input(
            "   Enter tip as percentage (e.g., 10) or amount (e.g., ₹50): "
        ).strip()

        if "%" in tip_choice or tip_choice.replace(".", "").isdigit():
            tip_value = float(tip_choice.replace("%", "").replace("₹", "").strip())

            if "%" in tip_choice or tip_value <= 100:
                tip_amount = (total_bill * tip_value) / 100
                print(f"   ✅ Adding {tip_value}% tip: ₹{tip_amount:.2f}")
            else:
                tip_amount = tip_value
                print(f"   ✅ Adding tip: ₹{tip_amount:.2f}")

    grand_total = total_bill + tip_amount
    share_per_person = round(grand_total / num_people, 2)

    print_summary_box(names, total_bill, tip_amount, grand_total, share_per_person)

    print("\n" + "🎉 Thank you for using Bill Splitter Pro! 🎉".center(60))
    print("=" * 60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Program cancelled by user. Goodbye! 👋")
    except Exception as e:
        print(f"\n\n❌ An unexpected error occurred: {e}")
        print("Please try again.")
