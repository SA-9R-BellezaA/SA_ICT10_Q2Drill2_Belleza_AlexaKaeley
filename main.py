from pyscript import document

# I really like spongebob, so I decided to do a spongebob themed drill 2
krusty_regulars = {"Patrick Star", "Sandy Cheeks", "Mrs. Puff", "Larry Lobster"}
fancy_diners = {"Squilliam Fancyson", "Bubble Bass", "Larry Lobster"}
bikini_bottom_heroes = {"Mermaid Man", "Barnacle Boy", "Sandy Cheeks"}
sneaky_visitors = {"Sheldon Plankton", "Old Man Jenkins", "Bubble Bass"}


master_set = krusty_regulars | fancy_diners | bikini_bottom_heroes | sneaky_visitors


def show_results():
    members = "<br>".join(sorted(master_set))
    document.querySelector("#output").innerHTML = (
        f"<strong>All members:</strong><br>{members}<br><br>"
        f"<strong>Total number of members:</strong> {len(master_set)}"
    )


def result_checker(event):
    global master_set
    first_name = document.querySelector("#first_name").value.strip()
    last_name = document.querySelector("#last_name").value.strip()

  
    new_member = {f"{first_name} {last_name}".strip().title()} - {""}
    

   # Master set holds every member in one place, and it is a set so no name can appear twice.
    master_set = master_set | new_member

    show_results()


show_results()
