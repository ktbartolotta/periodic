import Tkinter
import ttk
import ttkstyles
import periodic


class QuitButton(ttk.Button):

    """docstring for  QuitButton"""

    def __init__(self, parent):

        ttk.Button.__init__(
            self,
            parent,
            text="Quit",
            style="Quit.TButton"
        )


class ElementLabel(ttk.Label):

    """docstring for ElementLabel"""

    def __init__(self, parent, element):

        ttk.Label.__init__(
            self,
            parent,
            style="Element.TLabel")

        ttk.Label(
            self,
            text=element["name"],
            style="Name.Element.TLabel"
        ).pack()

        ttk.Label(
            self,
            text=element["atomic_no"],
            style="AtomicNo.Element.TLabel"
        ).pack()

        ttk.Label(
            self,
            text=element["symbol"],
            style="Symbol.Element.TLabel"
        ).pack(side=Tkinter.TOP)

        ttk.Label(
            self,
            text=element["atomic_wt"],
            style="AtomiWt.Element.TLabel"
        ).pack()


class Application(ttk.Frame):

    """docstring for Application"""

    def __init__(self, parent):

        ttk.Frame.__init__(self, parent)
        ttkstyles.load_styles()
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        elements = periodic.get_periodics("bacon")
        for match in elements:
            holder = ttk.Label(self)
            for el in match:
                ElementLabel(
                    holder, el
                ).pack(side=Tkinter.LEFT, padx=5, pady=5)
            holder.pack()


if __name__ == "__main__":
    root = Tkinter.Tk()
    root.geometry(
        "".join(
            [
                str(root.winfo_screenwidth()), "x",
                str(root.winfo_screenheight()),
                "+0+0"
            ]
        )
    )
    app = Application(parent=root)
    root.mainloop()