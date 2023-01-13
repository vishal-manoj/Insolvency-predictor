from tkinter import *
from financial_data import FinancialData, ReportGenerator
from tkinter import filedialog


class Application:
    def __init__(self, root):
        self.company_name_label = None
        self.year_label = None
        self.no_shares_label = None
        self.rfo_label = None
        self.credit_sales_label = None
        self.oi_label = None
        self.depreciation_amortization_label = None
        self.cost_of_goods_label = None
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
        self.net_income_flag_label = None
        self.company_data = None
        self.submit_label = None

        self.company_name_entry = None
        self.year_entry = None
        self.no_shares_entry = None
        self.rfo_entry = None
        self.credit_sales_entry = None
        self.oi_entry = None
        self.depreciation_amortization_entry = None
        self.cost_of_goods_entry = None
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
        self.selected_option = None
        self.option_values = None
        self.net_income_flag_radio1 = None
        self.net_income_flag_radio2 = None
        self.report = None
        self.report_text = None
        self.path = None
        self.pdf_report = None
        self.data_entry_frame = None
        self.report_frame = None
        self.submit_button_frame = None
        self.submit_button = None

        self.root = root
        self.root.title('Insolvency Predictor')
        self.root.state('zoomed')
        self.root.name_label = Label(self.root, text='Insolvency Predictor', bg='#31f1f7', width=180, height=2, font=10)
        self.root.name_label.place(x=0, y=0)
        self.button_frame = Frame(self.root, height=740, width=300, highlightbackground='#31f1f7', highlightthickness=4)
        self.button_frame.place(x=0, y=50)
        self.display_frame = Frame(self.root, height=740, width=1235, highlightbackground='#31f1f7',
                                   highlightthickness=4)
        self.display_frame.place(x=300, y=50)

        self.data_button = Button(self.button_frame, text='Enter Data', height=3, width=40, bg='#31f1f7',
                                  command=self.data_space)
        self.report_button = Button(self.button_frame, text='Show Insolvency Report', height=3, width=40, bg='#31f1f7',
                                    command=self.show_insolvency_report)
        self.save_report_button = Button(self.button_frame, text='Save Report', height=3, width=40, bg='#31f1f7',
                                         state=DISABLED, command=self.save_report)

        self.clear_button = Button(self.button_frame, text='Clear Data', height=3, width=40, bg='#31f1f7',
                                   command=self.clear_data)
        # a list of buttons is created and is placed with a loop so that the position of all buttons can be controlled
        # from a loop
        button_list = [self.data_button, self.report_button, self.save_report_button, self.clear_button]
        button_y = 2
        for button in button_list:
            button.place(x=1, y=button_y)
            button_y += 100
        self.enter_data_label = Label(self.display_frame, text='Click On Enter Data Button to Enter Financial Data',
                                      font=('Arial', 16))
        self.enter_data_label.place(x=400, y=250)

    def data_space(self):
        self.enter_data_label.destroy()
        self.data_entry_frame = Frame(self.display_frame, height=740, width=1230, highlightbackground='#31f1f7',
                                      highlightthickness=4)
        self.data_entry_frame.place(x=0, y=0)
        self.submit_button_frame = Frame(self.data_entry_frame, height=70, width=1230, highlightbackground='#31f1f7',
                                         highlightthickness=4)

        self.submit_button_frame.place(x=0, y=665)
        self.submit_button = Button(self.submit_button_frame, text='Submit Data', height=3, width=30, bg='#31f1f7',
                                    command=self.submit)
        self.submit_button.place(x=500, y=3)

        size = ('Arial', 12)
        # Labels for data entry boxes
        self.company_name_label = Label(self.data_entry_frame, text='Company Name:', font=size)
        self.year_label = Label(self.data_entry_frame, text='Year:', font=size)
        self.no_shares_label = Label(self.data_entry_frame, text='Number of shares:', font=size)
        self.rfo_label = Label(self.data_entry_frame, text='Revenue From Operations:', font=size)
        self.credit_sales_label = Label(self.data_entry_frame, text='Credit Sales:', font=size)
        self.oi_label = Label(self.data_entry_frame, text='Other Income:', font=size)
        self.depreciation_amortization_label = Label(self.data_entry_frame, text='Depreciation and Amortization:',
                                                     font=size)
        self.cost_of_goods_label = Label(self.data_entry_frame, text='Cost of goods sold:', font=size)
        self.operating_exp_label = Label(self.data_entry_frame, text='Operating Expenses:', font=size)
        self.finance_cost_label = Label(self.data_entry_frame, text='Finance Cost:', font=size)
        self.tax_amount_label = Label(self.data_entry_frame, text='Tax Amount:', font=size)

        self.contingent_liability_label = Label(self.data_entry_frame, text='Contingent Liabilities:', font=size)
        self.total_asset_label = Label(self.data_entry_frame, text='Total Asset:', font=size)
        self.retained_earnings_label = Label(self.data_entry_frame, text='Retained earnings:', font=size)
        self.equity_capital_label = Label(self.data_entry_frame, text='Equity Capital:', font=size)
        self.long_term_debt_label = Label(self.data_entry_frame, text='Long Term Debt :', font=size)
        self.current_asset_label = Label(self.data_entry_frame, text='Current Asset:', font=size)
        self.marketable_securities_label = Label(self.data_entry_frame, text='Marketable Securities:', font=size)
        self.trade_receivables_label = Label(self.data_entry_frame, text='Trade Receivables:', font=size)
        self.inventory_label = Label(self.data_entry_frame, text='Inventory:', font=size)
        self.current_liability_label = Label(self.data_entry_frame, text='Current Liability:', font=size)
        self.cash_equivalents_label = Label(self.data_entry_frame, text='Cash and Cash Equivalents:', font=size)

        self.cash_flow_label = Label(self.data_entry_frame, text='Cash Flow:', font=size)
        self.operating_cashflow_label = Label(self.data_entry_frame, text='Operating Cash Flow:', font=size)
        self.net_income_flag_label = Label(self.data_entry_frame,
                                           text='Negative net income for last two consecutive years:',
                                           font=size)

        # Entry boxes for entering data
        width = 50
        self.company_name_entry = Entry(self.data_entry_frame, width=width)
        self.year_entry = Entry(self.data_entry_frame, width=width)
        self.no_shares_entry = Entry(self.data_entry_frame, width=width)
        self.rfo_entry = Entry(self.data_entry_frame, width=width)
        self.credit_sales_entry = Entry(self.data_entry_frame, width=width)
        self.oi_entry = Entry(self.data_entry_frame, width=width)
        self.depreciation_amortization_entry = Entry(self.data_entry_frame, width=width)
        self.cost_of_goods_entry = Entry(self.data_entry_frame, width=width)
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
        self.selected_option = IntVar()
        self.net_income_flag_radio1 = Radiobutton(self.data_entry_frame, text='No', variable=self.selected_option,
                                                  value=0)
        self.net_income_flag_radio1.place(x=400, y=615)
        self.net_income_flag_radio2 = Radiobutton(self.data_entry_frame, text='Yes', variable=self.selected_option,
                                                  value=1)
        self.net_income_flag_radio2.place(x=500, y=615)
        label_list = [self.company_name_label, self.year_label, self.no_shares_label, self.rfo_label,
                      self.credit_sales_label, self.oi_label, self.depreciation_amortization_label,
                      self.cost_of_goods_label, self.operating_exp_label, self.finance_cost_label,
                      self.tax_amount_label, self.contingent_liability_label, self.total_asset_label,
                      self.retained_earnings_label, self.equity_capital_label, self.long_term_debt_label,
                      self.current_asset_label, self.marketable_securities_label, self.trade_receivables_label,
                      self.inventory_label, self.current_liability_label, self.cash_equivalents_label,
                      self.cash_flow_label, self.operating_cashflow_label, self.net_income_flag_label]

        entry_list = [self.company_name_entry, self.year_entry, self.no_shares_entry, self.rfo_entry,
                      self.credit_sales_entry, self.oi_entry, self.depreciation_amortization_entry,
                      self.cost_of_goods_entry, self.operating_exp_entry, self.finance_cost_entry,
                      self.tax_amount_entry, self.contingent_liability_entry, self.total_asset_entry,
                      self.retained_earnings_entry, self.equity_capital_entry, self.long_term_debt_entry,
                      self.current_asset_entry, self.marketable_securities_entry, self.trade_receivables_entry,
                      self.inventory_entry, self.current_liability_entry, self.cash_equivalents_entry,
                      self.cash_flow_entry, self.operating_cashflow_entry]

        # for loop is used to place labels and buttons. So, position of all labels and entry boxes can be controlled
        # from a loop.
        label_y = 10
        for label in label_list:
            label.place(x=5, y=label_y)
            label_y += 25
        entry_y = 10
        for entry in entry_list:
            entry.place(x=400, y=entry_y)
            entry_y += 25

    def submit(self):
        # Class FinancialData will be initialized with the values input in the entry boxes by the user.
        self.company_data = FinancialData(name=self.company_name_entry.get(), year=self.year_entry.get(),
                                          no_of_shares=int(self.no_shares_entry.get()), rfo=int(self.rfo_entry.get()),
                                          credit_sales=int(self.credit_sales_entry.get()), oi=int(self.oi_entry.get()),
                                          cgs=int(self.cost_of_goods_entry.get()),
                                          oex=int(self.operating_exp_entry.get()),
                                          da=int(self.depreciation_amortization_entry.get()),
                                          fc=int(self.finance_cost_entry.get()), tax=int(self.tax_amount_entry.get()),
                                          cl=int(self.contingent_liability_entry.get()),
                                          total_asset=int(self.total_asset_entry.get()),
                                          re=int(self.retained_earnings_entry.get()),
                                          equity=int(self.equity_capital_entry.get()),
                                          ltd=int(self.long_term_debt_entry.get()),
                                          current_asset=int(self.current_asset_entry.get()),
                                          securities=int(self.marketable_securities_entry.get()),
                                          tr=int(self.trade_receivables_entry.get()),
                                          inventory=int(self.inventory_entry.get()),
                                          current_liability=int(self.current_liability_entry.get()),
                                          cac=int(self.cash_equivalents_entry.get()),
                                          cf=int(self.cash_flow_entry.get()),
                                          ocf=int(self.operating_cashflow_entry.get()),
                                          net_income_flag=int(self.selected_option.get()))
        for widget in self.data_entry_frame.winfo_children():
            widget.destroy()
        self.submit_label = Label(self.display_frame, text='Data  Successfully Submitted', font=('Arial', 18))
        self.submit_label.place(x=400, y=250)

    def show_insolvency_report(self):
        self.submit_label.destroy()
        self.report_frame = Frame(self.display_frame, height=740, width=1230, highlightbackground='#31f1f7',
                                  highlightthickness=4)
        self.report_frame.place(x=0, y=0)
        self.company_data.prediction_model()
        self.company_data.generate_report()
        self.report = self.company_data.insolvency_report
        self.report_text = Text(self.report_frame, font=('Arial', 12), height=40, width=136)
        self.report_text.insert(INSERT, self.company_data.insolvency_report)
        self.report_text.place(x=0, y=0)
        self.save_report_button['state'] = NORMAL
        self.report_text['state'] = DISABLED

    def save_report(self):
        self.path = filedialog.askdirectory(title='Select Location')
        self.pdf_report = ReportGenerator(path=self.path, report_data=self.company_data.insolvency_report,
                                          company=self.company_data.company_name)
        self.pdf_report.save()

    def clear_data(self):
        for widget in self.report_frame.winfo_children():
            widget.destroy()
        self.enter_data_label = Label(self.display_frame, text='Click On Enter Data Button to Enter Financial Data',
                                      font=('Arial', 16))
        self.enter_data_label.place(x=400, y=250)
        self.save_report_button['state'] = DISABLED





