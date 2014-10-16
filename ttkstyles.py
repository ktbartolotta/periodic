import ttk


def load_styles():

    ttk.Style().theme_use("clam")

    ttk.Style().configure(
        "Element.TLabel",
        background="white"
    )

    ttk.Style().configure(
        "Symbol.Element.TLabel",
        font=("Segoe UI", 32),
    )

    ttk.Style().configure(
        "AtomicNo.Element.TLabel",
        font=("Segoe UI", 20)
    )

    ttk.Style().configure(
        "Name.Element.TLabel",
        font=("Segoe UI", 14)
    )

    ttk.Style().configure(
        "AtomiWt.Element.TLabel",
        font=("Segoe UI", 14)
    )

    ttk.Style().configure(
        "Quit.TButton",
        background="red",
        forground="white",
        font=("Arial", 16)
    )
