from pyscript import document

# Krusty Krab customers, I wanted to do one of my favorite cartoons for this, so I decided to do a spongebob themed drill 2.
customers = [
    {"first": "Patrick", "last": "Star", "order": "Krabby Patty with extra Krabby Patties"},
    {"first": "Sandy", "last": "Cheeks", "order": "Krabby Patty only, no buns"},
    {"first": "Mrs.", "last": "Puff", "order": "Krabby Patty and a large Kelp Shake"},
    {"first": "Larry", "last": "Lobster", "order": "Double Krabby Patty with Coral Bits"},
    {"first": "Squilliam", "last": "Fancyson", "order": "Deluxe Krabby Patty, NO grease"},
    {"first": "Bubble", "last": "Bass", "order": "Triple Krabby Patty with extra pickles"},
    {"first": "Mermaid", "last": "Man", "order": "Krabby Patty and Salad"},
    {"first": "Barnacle", "last": "Boy", "order": "Krabby Patty"},
    {"first": "Sheldon", "last": "Plankton", "order": "The Secret Formula"},
    {"first": "Old Man", "last": "Jenkins", "order": "Krabby Patty"},
]


def find_customer(first_name, last_name):
    """Return the customer dict if the name matches, otherwise None."""
    for customer in customers:
        if (customer["first"].lower() == first_name.lower()
                and customer["last"].lower() == last_name.lower()):
            return customer
    return None


def result_checker(event):
    first_name = document.querySelector("#first_name").value.strip()
    last_name = document.querySelector("#last_name").value.strip()
    output = document.querySelector("#output")

    if not first_name or not last_name:
        output.innerText = "Please enter both a first name and a last name!"
        return

    customer = find_customer(first_name, last_name)

    if customer:
        output.innerText = (
            f"Welcome to the Krusty Krab, {customer['first']} {customer['last']}! "
            f"Your usual: {customer['order']}."
        )
    else:
        names = ", ".join(f"{c['first']} {c['last']}" for c in customers)
        output.innerText = (
            f"Sorry, {first_name} {last_name} isn't a Krusty Krab customer. "
            f"Regulars: {names}."
        )