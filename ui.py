from tkinter import *


class Ui:
    def __init__(self, root):
        self.rfo_label = None
        self.oi_label = None
        self.depreciation_amortization_label = None
        self.operating_exp_label = None
        self.finance_cost_label = None
        self.tax_amount_label = None
        self.total_asset_label = None
        self.equity_capital_label = None
        self.long_term_debt_label = None
        self.current_asset_label = None
        self.current_liability_label = None
        self.cash_equivalents_label = None
        self.cash_flow_label = None
        self.operating_cashflow_label = None

        self.rfo_entry = None
        self.oi_entry = None
        self.depreciation_amortization_entry = None
        self.operating_exp_entry = None
        self.finance_cost_entry = None
        self.tax_amount_entry = None
        self.total_asset_entry = None
        self.equity_capital_entry = None
        self.long_term_debt_entry = None
        self.current_asset_entry = None
        self.current_liability_entry = None
        self.cash_equivalents_entry = None
        self.cash_flow_entry = None
        self.operating_cashflow_entry = None
        self.root = root
        self.root.title('Insolvency Predictor')
        self.root.state('zoomed')
        self.root.name_label = Label(self.root, text='Insolvency Predictor', bg='#31f1f7', width=140, height=2, font=10)
        self.root.name_label.place(x=0, y=0)
        self.button_frame = Frame(self.root, height=740, width=300, highlightbackground='#31f1f7', highlightthickness=4)
        self.button_frame.place(x=0, y=50)
        self.display_frame = Frame(self.root, height=740, width=1235, highlightbackground='#31f1f7',
                                   highlightthickness=4)
        self.display_frame.place(x=300, y=50)
        self.data_button = Button(self.button_frame, text='Enter Data', height=3, width=40, bg='#31f1f7',
                                  command=self.data_space)
        self.pl_button = Button(self.button_frame, text='Display P/L Statement', height=3, width=40, bg='#31f1f7')
        self.bs_button = Button(self.button_frame, text='Display Balance sheet', height=3, width=40, bg='#31f1f7')
        self.report_button = Button(self.button_frame, text='Show Insolvency Report', height=3, width=40, bg='#31f1f7')
        self.save_report_button = Button(self.button_frame, text='Save Report', height=3, width=40, bg='#31f1f7')
        self.clear_button = Button(self.button_frame, text='Clear Data', height=3, width=40, bg='#31f1f7')
        button_list = [self.data_button, self.pl_button, self.bs_button, self.report_button, self.save_report_button,
                       self.clear_button]
        button_y = 2
        for button in button_list:
            button.place(x=1, y=button_y)
            button_y += 100

    def data_space(self):
        size = ('Arial', 12)
        self.rfo_label = Label(self.display_frame, text='Revenue From Operations:', font=size)
        self.oi_label = Label(self.display_frame, text='Other Income:', font=size)
        self.depreciation_amortization_label = Label(self.display_frame, text='Depreciation and Amortization:',
                                                     font=size)
        self.operating_exp_label = Label(self.display_frame, text='Operating Expenses:', font=size)
        self.finance_cost_label = Label(self.display_frame, text='Finance Cost:', font=size)
        self.tax_amount_label = Label(self.display_frame, text='Tax Amount:', font=size)

        self.total_asset_label = Label(self.display_frame, text='Total Asset:', font=size)
        self.equity_capital_label = Label(self.display_frame, text='Total Asset:', font=size)
        self.long_term_debt_label = Label(self.display_frame, text='Total Asset:', font=size)
        self.current_asset_label = Label(self.display_frame, text='Current Asset:', font=size)
        self.current_liability_label = Label(self.display_frame, text='Current Liability:', font=size)
        self.cash_equivalents_label = Label(self.display_frame, text='Cash and Cash Equivalents:', font=size)

        self.cash_flow_label = Label(self.display_frame, text='Cash Flow:', font=size)
        self.operating_cashflow_label = Label(self.display_frame, text='Operating Cash Flow:', font=size)

        width = 50
        self.rfo_entry = Entry(self.display_frame, width=width)
        self.oi_entry = Entry(self.display_frame, width=width)
        self.depreciation_amortization_entry = Entry(self.display_frame, width=width)
        self.operating_exp_entry = Entry(self.display_frame, width=width)
        self.finance_cost_entry = Entry(self.display_frame, width=width)
        self.tax_amount_entry = Entry(self.display_frame, width=width)
        self.total_asset_entry = Entry(self.display_frame, width=width)
        self.equity_capital_entry = Entry(self.display_frame, width=width)
        self.long_term_debt_entry = Entry(self.display_frame, width=width)
        self.current_asset_entry = Entry(self.display_frame, width=width)
        self.current_liability_entry = Entry(self.display_frame, width=width)
        self.cash_equivalents_entry = Entry(self.display_frame, width=width)
        self.cash_flow_entry = Entry(self.display_frame, width=width)
        self.operating_cashflow_entry = Entry(self.display_frame, width=width)

        label_list = [self.rfo_label, self.oi_label, self.depreciation_amortization_label, self.operating_exp_label,
                      self.finance_cost_label, self.tax_amount_label, self.total_asset_label, self.equity_capital_label,
                      self.long_term_debt_label, self.current_asset_label, self.current_liability_label,
                      self.cash_equivalents_label, self.cash_flow_label, self.operating_cashflow_label]

        entry_list = [self.rfo_entry, self.oi_entry, self.depreciation_amortization_entry, self.operating_exp_entry,
                      self.finance_cost_entry, self.tax_amount_entry, self.total_asset_entry, self.equity_capital_entry,
                      self.long_term_debt_entry, self.current_asset_entry, self.current_liability_entry,
                      self.cash_equivalents_entry, self.cash_flow_entry, self.operating_cashflow_entry]
        label_y = 20
        for label in label_list:
            label.place(x=5, y=label_y)
            label_y += 50
        entry_y = 20
        for entry in entry_list:
            entry.place(x=400, y=entry_y)
            entry_y += 50


obj = Tk()
master = Ui(obj)
obj.mainloop()



