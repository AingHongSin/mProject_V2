import itertools
from tkinter import *
from tkinter import messagebox
from tkmacosx import Button, CircleButton, SFrame

FONT = ('Pacifico', 28, 'bold')
BACKGROUND_COLOR = "#E6E6E6"
TITLE_COLOR = "#707070"
SEARCH_LABEL_FONT = ('Pacifico', 22, 'bold')


class UI:

    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.title("TRANSACTION CLEARER")
        self.mainWindow.config(background=BACKGROUND_COLOR)
        self.mainWindow.config(pady=10)
        self.mainWindow.resizable(False, False)

        # Variable Section
        self.amountSlot = 0

        self.global_variable()

        # Frame Section
        self.topFrame = Frame(self.mainWindow, bg=BACKGROUND_COLOR)
        self.topFrame.pack(fill='x', side='top', padx=10)

        self.inputFrame_topFrame = SFrame(self.topFrame, width=498)
        self.inputFrame_topFrame.pack(side='bottom')

        self.middleFrame = Frame(self.mainWindow, bg=BACKGROUND_COLOR)
        self.middleFrame.pack(fill='x', padx=10)

        self.bottomFrame = Frame(self.mainWindow, bg=BACKGROUND_COLOR)
        self.bottomFrame.pack(fill='x', padx=10)

        self.displayLabelFrame = LabelFrame(self.bottomFrame, text='Display Result', bg=BACKGROUND_COLOR,
                                            relief='ridge')
        self.displayLabelFrame.pack(side='bottom')

        self.displayFrame = SFrame(self.displayLabelFrame, width=498)
        self.displayFrame.pack(side='bottom', padx=10, pady=15)

        # Widget
        self.title_Application = Label(self.topFrame, text="Transaction Clearer", font=FONT, fg=TITLE_COLOR,
                                       bg=BACKGROUND_COLOR)
        self.title_Application.pack(fill='x')
        self.title_Application.bind("<Button-1>", self.resetData)

        self.addButton = CircleButton(self.topFrame, text='➕', width=30, borderless=5)
        self.addButton.config(command=self.addSlot_Function)
        self.addButton.pack(side='right')

        # self.slotInput()

        self.searchMessageLabel = Label(self.middleFrame, text='Search: ', font=SEARCH_LABEL_FONT)
        self.searchMessageLabel.config(fg=TITLE_COLOR, bg=BACKGROUND_COLOR)
        self.searchMessageLabel.pack(side='left', pady=10)

        self.searchInputEntry = Entry(self.middleFrame, width=19, highlightthickness=0, relief='flat',
                                      font=('defult', 22))
        self.searchInputEntry.pack(side='left', pady=10, padx=15)
        self.searchInputEntry.bind("<Return>", self.EnterBindingKey)

        self.calculateButton = Button(self.middleFrame, text='Calculate', font=('Pacifico', 14), fg=TITLE_COLOR)
        self.calculateButton.config(width=120, height=33, borderless=5)
        self.calculateButton.config(command=self.calculate_and_dislplay)
        self.calculateButton.pack(side='right', pady=10)

        self.mainWindow.mainloop()

    def global_variable(self):

        self.valueListVar = []
        self.entryWidgetVar = []
        self.listSlot = []
        self.h = False

    def slotInput(self):

        Box_Slot = f"Frame {len(self.listSlot)}"
        Box_Slot = Button(self.inputFrame_topFrame, borderless=5, pady=5, state='disable')
        Box_Slot.pack(padx=5, pady=5)
        self.slotLabelName = f"Slot {len(self.listSlot)}"
        self.slotLabelName = Label(Box_Slot, text=f"Slot {self.amountSlot}", font=('Pacifico', 14))
        self.slotLabelName.grid(row=0, column=0, padx=5, pady=10)

        slotEntryValue = f"Slot {len(self.listSlot)}"
        slotEntryValue = Entry(Box_Slot, width=25, font=('default', 22))
        slotEntryValue.grid(row=0, column=1)
        slotEntryValue.focus()

        self.entryWidgetVar.append(slotEntryValue)

        self.deleteSlotButton = CircleButton(Box_Slot, text='➖', width=30, borderless=5)
        self.deleteSlotButton.config(command=lambda slot=Box_Slot: self.deleteSlot_Function(slot))
        self.deleteSlotButton.grid(row=0, column=2, padx=10)

    def EnterBindingKey(self, event):
        self.calculate_and_dislplay()

    def addSlot_Function(self):

        self.amountSlot += 1
        self.listSlot.append(f"Slot {self.amountSlot} :")
        self.slotInput()

    def deleteSlot_Function(self, box):
        global slotLabelName
        global slotEntryValue

        self.amountSlot -= 1
        # self.lastEntry = self.listSlot[-1]
        box.pack_forget()

    def checking(self, input_value):
        checking_var = ''
        if type(input_value) == list:
            for value in input_value:
                try:
                   self.valueListVar.append(float(value.get()))
                   checking_var = True
                except:
                    messagebox.showwarning("Warning", f"Please enter number in slots. {value.get()} is not a number.")
                    checking_var = False
                    break
                    self.global_variable()

        else:
            try:
                self.search_num = int(input_value)
                checking_var = True
            except:
                messagebox.showwarning("Warning", f"Please enter number in search slot. {input_value} is not a number.")
                checking_var = False

        return checking_var

    def resetData(self, event):
        self.mainWindow.destroy()
        self.__init__()

    def calculate_and_dislplay(self):
        if self.checking(self.entryWidgetVar):

            if self.checking(self.searchInputEntry.get()):
                self.mesDisplayUpper = Message(self.displayFrame, width=540)
                self.mesDisplayUpper.pack()
                self.mesDisplayUpper.config(text=f"All the data is corresponding sum and the data have :")

                if sum(self.valueListVar) == int(self.search_num):
                    self.mesTotal = Message(self.displayFrame, width=540)
                    self.mesTotal.pack()
                    self.mesTotal.config(text=f"Sum of all slots equal to the search amount")

                for a in range(len(self.valueListVar)):
                    print(a)
                    for b in itertools.combinations(self.valueListVar, a):
                        print(b)
                        if int(sum(b)) == self.search_num:
                            self.mesDisplay = Message(self.displayFrame, width=540, justify='left')
                            self.mesDisplay.pack()

                            self.mesDisplay.config( text=f"Which has {b}")
                            self.h = True


                if not self.h:
                    self.mesDisplay.config(text=("No Datas Found!"))

                self.global_variable()


if __name__ == '__main__':
    UI()
