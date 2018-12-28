from tkinter import Tk, Listbox, ttk, LabelFrame, Label, Entry
from locationList import locations
from item import items

def createComboBox(window, elements=[]):
    combo = ttk.Combobox(window)
    combo['values'] = list(elements)
    combo.current(0)
    return combo

def main():
    window = Tk()
    window.title("HintPad")
    window.geometry("600x600+500+100")

    locations.sort()
    items.sort()

    #Way the hero
    way = LabelFrame(window, text="Way the hero", padx=20, pady=20)
    way.pack(fill="both", expand="yes")

    for i in range(4):
        createComboBox(way, elements=locations).grid(row=int(i/2), column=i%2)
    
    #Barren of treasure
    barren = LabelFrame(window, text="Barren of treasure", padx=20, pady=20)
    barren.pack(fill="both", expand="yes")

    for i in range(2):
        createComboBox(barren, elements=locations).grid(row=int(i/2), column=i%2)

    #Other
    other = LabelFrame(window, text="Other", padx=20, pady=20)
    other.pack(fill="both", expand="yes")

    Label(other, text="30 skulls").grid(row=0, column=0)
    Label(other, text="40 skulls").grid(row=1, column=0)
    Label(other, text="50 skulls").grid(row=2, column=0)
    Label(other, text="Frogs").grid(row=3, column=0)
    Label(other, text="Big poes").grid(row=4, column=0)
    Label(other, text="Biggoron Sword").grid(row=5, column=0)

    for i in range(4):
        Entry(other, width=30).grid(row=i+6, column=0)

    for i in range(10):
        createComboBox(other, elements=items).grid(row=i, column=1)
    

    
    window.mainloop()

if __name__ == "__main__":
    main()