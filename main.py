from tkinter import Tk, Listbox, ttk, LabelFrame, Label, Entry, Checkbutton, BooleanVar, Button
from locationList import locations
from item import items, allitems

combosWithItem = []
combosForEntry = []
entries = []

def createComboBox(window, elements=[]):
    combo = ttk.Combobox(window)
    combo['values'] = list(elements)
    combo.current(0)
    return combo

def addEntry(window, value):
    elements = list(items) if value.get() else allitems
    entry = Entry(window, width=20)
    entry.grid(row=len(entries)+8, column=0)
    comboBox = createComboBox(window, elements)
    comboBox.grid(row=len(entries)+8, column=1)
    combosWithItem.append(comboBox)
    entries.append(entry)

def removeEntry():
    if len(entries) > 0:
        entries[-1].destroy()
        del entries[-1]
        combosWithItem[-1].destroy()
        del combosWithItem[-1]

def removeUseless(value):
    elements = list(items) if value.get() else allitems
    if value.get() :
        elements.insert(1,"Useless")
    for combo in combosWithItem:
        combo['values'] = list(elements)


def main():
    window = Tk()
    window.title("HintPad")
    window.geometry("600x600+500+100")

    locations.sort()
    items.sort()

    #Way the hero
    way = LabelFrame(window, text="Way the hero", padx=20, pady=20)
    way.pack(fill="both", expand="yes")
    Label(way, text="Locations").grid(row=0, column=0)
    Label(way, text="both").grid(row=0, column=1)
    for i in range(4):
        createComboBox(way, elements=locations).grid(row=i+1, column=0)
        Checkbutton(way).grid(row=i+1, column=1)
    
    #Barren of treasure
    barren = LabelFrame(window, text="Barren of treasure", padx=20, pady=20)
    barren.pack(fill="both", expand="yes")

    for i in range(2):
        createComboBox(barren, elements=locations).grid(row=int(i/2), column=i%2)

    #Other
    other = LabelFrame(window, text="Other", padx=20, pady=20)
    other.pack(fill="both", expand="yes")

    value = BooleanVar()
    value.set(True)
    check = Checkbutton(other, text="Remove useless item", variable=value, command=(lambda : removeUseless(value)))
    check.grid(row=0, column=0)

    Label(other, text="30 skulls").grid(row=1, column=0)
    Label(other, text="40 skulls").grid(row=2, column=0)
    Label(other, text="50 skulls").grid(row=3, column=0)
    Label(other, text="Frogs").grid(row=4, column=0)
    Label(other, text="Ocarina Of Time").grid(row=5, column=0)
    Label(other, text="Biggoron Sword").grid(row=6, column=0)

    for i in range(6):
        combo = createComboBox(other, elements=items)
        combosWithItem.append(combo)
        combo.grid(row=i+1, column=1)
    Button(other, text="+", command=lambda: addEntry(other, value)).grid(row=7, column=0)
    Button(other, text="-", command=removeEntry).grid(row=7, column=1)
    removeUseless(value)
    window.mainloop()

if __name__ == "__main__":
    main()