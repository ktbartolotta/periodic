import ttk


def load_styles():

    ttk.Style().theme_use("clam")

    ttk.Style().configure(
        "Element.TLabel",
        background="white"
    )

    ttk.Style().configure(
        "Symbol.Element.TLabel",
        font=("Segoe UI", 16, "bold")
    )

    ttk.Style().configure(
        "AtomicNo.Element.TLabel",
        font=("Segoe UI", 10)
    )

    ttk.Style().configure(
        "Name.Element.TLabel",
        font=("Segoe UI", 8)
    )

    ttk.Style().configure(
        "AtomicWt.Element.TLabel",
        font=("Segoe UI", 7)
    )

    ttk.Style().configure(
        "Quit.TButton",
        background="red",
        forground="white",
        font=("Arial", 8)
    )
