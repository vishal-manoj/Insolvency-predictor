from tkinter import *


class Ui:
    def __init__(self, root):
        self.company_name_label = None
        self.year_label = None
        self.no_shares_label = None
        self.rfo_label = None
        self.oi_label = None
        self.depreciation_amortization_label = None
        self.operating_exp_label = None
        self.finance_cost_label = None
        self.tax_amount_label = None
        self.contingent_liability_label = None
        self.total_asset_label = None
        self.retained_earnings_label = None
        self.equity_capital_label = None
        self.long_term_debt_label = None
        self.current_asset_label = None
        self.marketable_securities_label = None
        self.trade_receivables_label = None
        self.inventory_label = None
        self.current_liability_label = None
        self.cash_equivalents_label = None
        self.cash_flow_label = None
        self.operating_cashflow_label = None

        self.company_name_entry = None
        self.year_entry = None
        self.no_shares_entry = None
        self.rfo_entry = None
        self.oi_entry = None
        self.depreciation_amortization_entry = None
        self.operating_exp_entry = None
        self.finance_cost_entry = None
        self.tax_amount_entry = None
        self.contingent_liability_entry = None
        self.total_asset_entry = None
        self.retained_earnings_entry = None
        self.equity_capital_entry = None
        self.long_term_debt_entry = None
        self.current_asset_entry = None
        self.marketable_securities_entry = None
        self.trade_receivables_entry = None
        self.inventory_entry = None
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

        self.data_entry_frame = Frame(self.display_frame, height=740, width=1230, highlightbackground='#31f1f7',
                                      highlightthickness=4)
        self.data_entry_frame.place(x=0, y=0)

        self.submit_button_frame = Frame(self.display_frame, height=70, width=1230, highlightbackground='#31f1f7',
                                         highlightthickness=4)
        self.submit_button_frame.place(x=0, y=665)
        self.submit_button = Button(self.submit_button_frame, text='Submit Data', height=3, width=30, bg='#31f1f7')
        self.submit_button.place(x=500, y=3)
        self.data_button = Button(self.button_frame, text='Enter Data', height=3, width=40, bg='#31f1f7',
                                  command=self.data_space)
        self.report_button = Button(self.button_frame, text='Show Insolvency Report', height=3, width=40, bg='#31f1f7')
        self.save_report_button = Button(self.button_frame, text='Save Report', height=3, width=40, bg='#31f1f7')
        self.clear_button = Button(self.button_frame, text='Clear Data', height=3, width=40, bg='#31f1f7')
        button_list = [self.data_button, self.report_button, self.save_report_button, self.clear_button]
        button_y = 2
        for button in button_list:
            button.place(x=1, y=button_y)
            button_y += 100

    def data_space(self):
        size = ('Arial', 12)
        self.company_name_label = Label(self.data_entry_frame, text='Company Name:', font=size)
        self.year_label = Label(self.data_entry_frame, text='Year:', font=size)
        self.no_shares_label = Label(self.data_entry_frame, text='Number of shares:', font=size)
        self.rfo_label = Label(self.data_entry_frame, text='Revenue From Operations:', font=size)
        self.oi_label = Label(self.data_entry_frame, text='Other Income:', font=size)
        self.depreciation_amortization_label = Label(self.data_entry_frame, text='Depreciation and Amortization:',
                                                     font=size)
        self.operating_exp_label = Label(self.data_entry_frame, text='Operating Expenses:', font=size)
        self.finance_cost_label = Label(self.data_entry_frame, text='Finance Cost:', font=size)
        self.tax_amount_label = Label(self.data_entry_frame, text='Tax Amount:', font=size)

        self.contingent_liability_label = Label(self.data_entry_frame, text='Contingent Liabilities:', font=size)
        self.total_asset_label = Label(self.data_entry_frame, text='Total Asset:', font=size)
        self.retained_earnings_label = Label(self.data_entry_frame, text='Retained earnings:', font=size)
        self.equity_capital_label = Label(self.data_entry_frame, text='Total Asset:', font=size)
        self.long_term_debt_label = Label(self.data_entry_frame, text='Total Asset:', font=size)
        self.current_asset_label = Label(self.data_entry_frame, text='Current Asset:', font=size)
        self.marketable_securities_label = Label(self.data_entry_frame, text='Marketable Securities:', font=size)
        self.trade_receivables_label = Label(self.data_entry_frame, text='Trade Receivables:', font=size)
        self.inventory_label = Label(self.data_entry_frame, text='Inventory:', font=size)
        self.current_liability_label = Label(self.data_entry_frame, text='Current Liability:', font=size)
        self.cash_equivalents_label = Label(self.data_entry_frame, text='Cash and Cash Equivalents:', font=size)

        self.cash_flow_label = Label(self.data_entry_frame, text='Cash Flow:', font=size)
        self.operating_cashflow_label = Label(self.data_entry_frame, text='Operating Cash Flow:', font=size)

        width = 50
        self.company_name_entry = Entry(self.data_entry_frame, width=width)
        self.year_entry = Entry(self.data_entry_frame, width=width)
        self.no_shares_entry = Entry(self.data_entry_frame, width=width)
        self.rfo_entry = Entry(self.data_entry_frame, width=width)
        self.oi_entry = Entry(self.data_entry_frame, width=width)
        self.depreciation_amortization_entry = Entry(self.data_entry_frame, width=width)
        self.operating_exp_entry = Entry(self.data_entry_frame, width=width)
        self.finance_cost_entry = Entry(self.data_entry_frame, width=width)
        self.tax_amount_entry = Entry(self.data_entry_frame, width=width)

        self.contingent_liability_entry = Entry(self.data_entry_frame, width=width)
        self.total_asset_entry = Entry(self.data_entry_frame, width=width)
        self.retained_earnings_entry = Entry(self.data_entry_frame, width=width)
        self.equity_capital_entry = Entry(self.data_entry_frame, width=width)
        self.long_term_debt_entry = Entry(self.data_entry_frame, width=width)
        self.current_asset_entry = Entry(self.data_entry_frame, width=width)
        self.marketable_securities_entry = Entry(self.data_entry_frame, width=width)
        self.trade_receivables_entry = Entry(self.data_entry_frame, width=width)
        self.inventory_entry = Entry(self.data_entry_frame, width=width)
        self.current_liability_entry = Entry(self.data_entry_frame, width=width)
        self.cash_equivalents_entry = Entry(self.data_entry_frame, width=width)
        self.cash_flow_entry = Entry(self.data_entry_frame, width=width)
        self.operating_cashflow_entry = Entry(self.data_entry_frame, width=width)
        label_list = [self.company_name_label, self.year_label, self.no_shares_label, self.rfo_label, self.oi_label,
                      self.depreciation_amortization_label, self.operating_exp_label, self.finance_cost_label,
                      self.tax_amount_label, self.contingent_liability_label, self.total_asset_label,
                      self.retained_earnings_label, self.equity_capital_label, self.long_term_debt_label,
                      self.current_asset_label, self.marketable_securities_label, self.trade_receivables_label,
                      self.inventory_label, self.current_liability_label, self.cash_equivalents_label,
                      self.cash_flow_label, self.operating_cashflow_label]

        entry_list = [self.company_name_entry, self.year_entry, self.no_shares_entry, self.rfo_entry, self.oi_entry,
                      self.depreciation_amortization_entry, self.operating_exp_entry, self.finance_cost_entry,
                      self.tax_amount_entry, self.contingent_liability_entry, self.total_asset_entry,
                      self.retained_earnings_entry, self.equity_capital_entry, self.long_term_debt_entry,
                      self.current_asset_entry, self.marketable_securities_entry, self.trade_receivables_entry,
                      self.inventory_entry, self.current_liability_entry, self.cash_equivalents_entry,
                      self.cash_flow_entry, self.operating_cashflow_entry]

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



