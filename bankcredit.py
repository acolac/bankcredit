from tkinter import *      

class LoanCalculator:
	def __init__(self):    
		window = Tk() 
		window.title("Bank Credit - Calculator") 
		window.configure(background = "aliceblue") 

		Label(window, font='Verdana 10',bg ="aliceblue",text="Annual Interest Rate").grid(row=1,column=1, sticky=W)
		Label(window, font='Verdana 10',bg ="aliceblue",text="N& of Years").grid(row=2,column=1, sticky=W)
		Label(window, font='Verdana 10',bg ="aliceblue",text="Loan Amount").grid(row=3,column=1, sticky=W)
		Label(window, font='Verdana 10',bg ="aliceblue", text="Monthly Payment").grid(row=4,column=1, sticky=W)
		Label(window, font='Verdana 10',bg ="aliceblue",text="Total Payment").grid(row=5,column=1, sticky=W)
		Label(window, font='Verdana 10',bg ="aliceblue",text="Press on Go button to proceed").grid(row=6,column=1, sticky=W)
		Label(window, font='Verdana 10',bg ="aliceblue",text="Or clear if you wish to change values").grid(row=7,column=1, sticky=W)

		self.annualInterestRateVar = StringVar()
		Entry(window, textvariable=self.annualInterestRateVar,justify=RIGHT).grid(row=1, column=2)

		self.numberofYearsVar = StringVar()
		Entry(window, textvariable=self.numberofYearsVar,justify=RIGHT).grid(row=2, column=2)

		self.loanAmountVar = StringVar()
		Entry(window, textvariable=self.loanAmountVar,justify=RIGHT).grid(row=3, column=2)

		self.monthlyPaymentVar = StringVar()
		lblMonthlyPayment= Label(window,font='Verdana 10',bg ="aliceblue", textvariable=self.monthlyPaymentVar).grid(row=4,column=2, sticky=E)

		self.totalPaymentVar = StringVar()
		lblTotalPayment= Label(window,font='Verdana 10',bg ="aliceblue", textvariable=self.totalPaymentVar).grid(row=5,column=2, sticky=E)

		btComputePayment = Button(window, text="Go",bg="green",fg="white",font='Verdana 12 bold', command=self.computePayment).grid(row=6, column=2, sticky=E)
		btClear = Button(window, text="Clear",bg="grey",fg="white",font='Verdana 12 bold', command=self.delete_all).grid(row=7, column=3, padx=20,pady=20 ,sticky=E)

		window.mainloop()

	def computePayment(self):
		monthlyPayment = self.getMonthlyPayment(
			float(self.loanAmountVar.get()),
			float(self.annualInterestRateVar.get())  / 1200 ,
			int(self.numberofYearsVar.get()))

		self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
		totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
		 * int(self.numberofYearsVar.get())

		self.totalPaymentVar.set(format(totalPayment, '10.2f'))

	def getMonthlyPayment(self,loanAmount,monthlyInterestRate,numberofYears):
		monthlyPayment = loanAmount * monthlyInterestRate / (1-1/(1 + monthlyInterestRate)** (numberofYears * 12 ))
		return monthlyPayment	


	def delete_all(self) :
		self.monthlyPaymentVar.set("")
		self.loanAmountVar.set("")
		self.annualInterestRateVar.set("")
		self.numberofYearsVar.set("")
		self.totalPaymentVar.set("")

LoanCalculator()
