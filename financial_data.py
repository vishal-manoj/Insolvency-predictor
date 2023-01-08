import pandas as pd
import joblib


class FinancialData:
    def __init__(self, **kwargs):
        self.company_name = kwargs.get('name')
        self.year = kwargs.get('year')
        self.no_of_shares = kwargs.get('no_of_shares')
        self.revenue_from_operations = kwargs.get('rfo')
        self.credit_sales = kwargs.get('credit_sales')
        self.other_income = kwargs.get('oi')
        self.cost_goods_sold = kwargs.get('cgs')
        self.operating_expenses = kwargs.get('oex')
        self.depreciation_amortization = kwargs.get('da')
        self.finance_cost = kwargs.get('fc')
        self.tax_amount = kwargs.get('tax')
        self.contingent_liability = kwargs.get('cl')
        self.total_asset = kwargs.get('total_asset')
        self.retained_earnings = kwargs.get('re')
        self.equity_capital = kwargs.get('equity')
        self.long_term_debt = kwargs.get('ltd')
        self.current_asset = kwargs.get('current_asset')
        self.marketable_securities = kwargs.get('securities')
        self.trade_receivables = kwargs.get('tr')
        self.inventory = kwargs.get('inventory')
        self.current_liability = kwargs.get('current_liability')
        self.cash_cash_equivalents = kwargs.get('cac')
        self.cash_flow = kwargs.get('cf')
        self.operating_cash_flow = kwargs.get('ocf')
        self.net_income_flag = kwargs.get('net_income_flag')
        self.insolvency_prediction = None
        self.insolvency_report = None
        self.pdf_report = None
        self.columns = None
        self.column_data = None
        self.data = None
        self.model = None
        self.gross_profit = self.revenue_from_operations-self.cost_goods_sold
        self.total_income = self.revenue_from_operations + self.other_income
        self.total_expense = self.cost_goods_sold + self.operating_expenses + self.finance_cost + self.tax_amount
        self.net_profit = self.total_income - self.total_expense
        self.operating_income = self.total_income - (self.cost_goods_sold + self.operating_expenses)
        self.pbt = self.revenue_from_operations - (self.cost_goods_sold + self.operating_expenses + self.finance_cost)
        self.ebit = self.total_income - (self.cost_goods_sold + self.operating_expenses)

        self.gp_margin = self.gross_profit/self.revenue_from_operations
        self.operating_profit_ratio = self.operating_income/self.revenue_from_operations
        self.operating_exp_ratio = self.operating_income/self.revenue_from_operations
        self.cash_flow_rate = self.operating_cash_flow/self.current_liability
        self.debt_equity_ratio = self.long_term_debt/self.equity_capital
        self.cash_flow_per_share = self.cash_flow/self.no_of_shares
        self.revenue_per_share = self.revenue_from_operations/self.no_of_shares
        self.operating_profit_per_share = self.operating_income/self.no_of_shares
        self.pretax_income_per_share = self.pbt/self.no_of_shares
        self.current_ratio = self.current_asset/self.current_liability
        self.quick_ratio = (self.cash_cash_equivalents + self.marketable_securities +
                            self.trade_receivables)/self.current_liability
        self.interest_expense_ratio = self.finance_cost/(self.revenue_from_operations + self.other_income)
        self.networth_asset_ratio = self.equity_capital/self.total_asset
        self.long_term_fund_suitability = (self.long_term_debt + self.equity_capital)/(self.total_asset -
                                                                                       self.current_asset)
        self.contingent_liability_networth = self.contingent_liability/self.equity_capital
        self.inventory_receivables_equity = (self.inventory + self.trade_receivables)/self.equity_capital
        self.asset_turnover_ratio = self.revenue_from_operations/self.total_asset
        self.trade_receivables_turnover = self.credit_sales/self.trade_receivables
        self.avg_collection_days = self.trade_receivables_turnover/365
        self.inventory_turnover = self.cost_goods_sold/self.inventory
        self.working_capital_total_asset_ratio = (self.current_asset - self.current_liability)/self.total_asset
        self.quick_asset_total_asset_ratio = (self.cash_cash_equivalents + self.marketable_securities +
                                              self.trade_receivables)/self.total_asset
        self.current_asset_total_asset_ratio = self.current_asset/self.total_asset
        self.cash_asset_total_asset_ratio = self.cash_cash_equivalents/self.total_asset
        self.cash_current_liability_ratio = self.cash_cash_equivalents/self.current_liability
        self.inventory_working_capital_ratio = self.inventory/(self.current_asset + self.current_liability)
        self.inventory_current_liability_ratio = self.inventory/self.current_liability
        self.working_capital_equity_ratio = (self.current_asset + self.current_liability)/self.equity_capital
        self.current_liability_equity_ratio = self.current_liability/self.equity_capital
        self.retained_earnings_total_asset = self.retained_earnings/self.total_asset
        self.total_income_exp_ratio = self.total_income/self.total_expense
        self.total_exp_asset_ratio = self.total_expense/self.total_asset
        self.current_asset_turnover = self.current_asset/self.revenue_from_operations
        self.quick_asset_turnover = (self.cash_cash_equivalents + self.marketable_securities +
                                     self.trade_receivables)/self.revenue_from_operations
        self.working_capital_turnover = (self.current_asset - self.current_liability)/self.revenue_from_operations
        self.cash_turnover = self.cash_cash_equivalents/self.revenue_from_operations
        self.cashflow_sales_ratio = self.cash_flow/self.revenue_from_operations
        self.cashflow_asset_ratio = self.cash_flow/self.total_asset
        self.cfo_asset_ratio = self.operating_cash_flow/self.total_asset
        self.cashflow_equity_ratio = self.cash_flow/self.equity_capital
        self.net_income_total_asset_ratio = self.net_profit/self.total_asset
        self.interest_coverage_ratio = self.finance_cost/self.ebit

    def prediction_model(self):
        self.columns = [' Operating Gross Margin', ' Operating Profit Rate',
                        ' Operating Expense Rate', ' Cash flow rate',
                        ' Interest-bearing debt interest rate', ' Cash Flow Per Share',
                        ' Revenue Per Share (Yuan Â¥)',
                        ' Operating Profit Per Share (Yuan Â¥)',
                        ' Per Share Net profit before tax (Yuan Â¥)', ' Current Ratio',
                        ' Quick Ratio', ' Interest Expense Ratio', ' Net worth/Assets',
                        ' Long-term fund suitability ratio (A)',
                        ' Contingent liabilities/Net worth',
                        ' Inventory and accounts receivable/Net value',
                        ' Total Asset Turnover', ' Accounts Receivable Turnover',
                        ' Average Collection Days', ' Inventory Turnover Rate (times)',
                        ' Working Capital to Total Assets', ' Quick Assets/Total Assets',
                        ' Current Assets/Total Assets', ' Cash/Total Assets',
                        ' Cash/Current Liability', ' Inventory/Working Capital',
                        ' Inventory/Current Liability', ' Working Capital/Equity',
                        ' Current Liabilities/Equity',
                        ' Retained Earnings to Total Assets',
                        ' Total income/Total expense', ' Total expense/Assets',
                        ' Current Asset Turnover Rate', ' Quick Asset Turnover Rate',
                        ' Working capitcal Turnover Rate', ' Cash Turnover Rate',
                        ' Cash Flow to Sales', ' Cash Flow to Total Assets',
                        ' CFO to Assets', ' Cash Flow to Equity',
                        ' Net Income to Total Assets',
                        ' Interest Coverage Ratio (Interest expense to EBIT)',
                        ' Net Income Flag']
        self.column_data = [[self.gp_margin, self.operating_profit_ratio, self.operating_exp_ratio, self.cash_flow_rate,
                            self.debt_equity_ratio, self.cash_flow_per_share, self.revenue_per_share,
                            self.operating_profit_per_share, self.pretax_income_per_share, self.current_ratio,
                            self.quick_ratio, self.interest_expense_ratio, self.networth_asset_ratio,
                            self.long_term_fund_suitability, self.contingent_liability_networth,
                            self.inventory_receivables_equity, self.asset_turnover_ratio,
                            self.trade_receivables_turnover, self.avg_collection_days, self.inventory_turnover,
                            self.working_capital_total_asset_ratio, self.quick_asset_total_asset_ratio,
                            self.current_asset_total_asset_ratio, self.cash_asset_total_asset_ratio,
                            self.cash_current_liability_ratio, self.inventory_working_capital_ratio,
                            self.inventory_current_liability_ratio, self.working_capital_equity_ratio,
                            self.current_liability_equity_ratio, self.retained_earnings_total_asset,
                            self.total_income_exp_ratio, self.total_exp_asset_ratio, self.current_asset_turnover,
                            self.quick_asset_turnover, self.working_capital_turnover, self.cash_turnover,
                            self.cashflow_sales_ratio, self.cashflow_asset_ratio, self.cfo_asset_ratio,
                            self.cashflow_equity_ratio, self.net_income_total_asset_ratio, self.interest_coverage_ratio,
                            self.net_income_flag]]
        self.data = pd.DataFrame(columns=self.columns, data=self.column_data)
        self.model = joblib.load("C:\\Users\\DELL\\insolvency_prediction_model.pkl")
        self.insolvency_prediction = self.model.predict(self.data)

    def generate_report(self):
        if self.insolvency_prediction == 0:
            self.insolvency_report = f''' 
                        On the basis of the financial data of {self.company_name} for the year {self.year}, \n 
                        it has been predicted that the company will not become insolvent. The prediction has been made\n
                        on the basis of the machine learning model Random Forest Classifier. \n
                
                        Details of the machine Learning model:\n
                        For predicting whether the company will become insolvent or not Machine Learning model named \n
                        Random Forest Classifier has been used. The model has been trained on 43 ratios of 6819 \n
                        companies. \n
                        
                        Source of data for training Machine Learning model: Kaggle
                        
                        Accuracy of Model: 0.97 \n
                        True Positives: 1312 \n
                        False Positives: 1 \n
                        False Negative: 45 \n
                        True Negative: 6 \n
                        '''

        if self.insolvency_prediction == 1:
            self.insolvency_report = f''' 
                        On the basis of the financial data of {self.company_name} for the year {self.year}, \n
                        it has been predicted that the company will become insolvent. The prediction has been made \n
                        on the basis of the machine learning model Random Forest Classifier. \n

                        Details of the machine Learning model:\n
                        For predicting whether the company will become insolvent or not Machine Learning model named \n
                        Random Forest Classifier has been used. The model has been trained on 43 ratios of 6819 \n
                        companies. \n
                        
                        Source of data for training Machine Learning model: Kaggle \n
                        
                        Accuracy of Model: 0.97 \n
                        True Positives: 1312 \n
                        False Positives: 1 \n
                        False Negative: 45 \n
                        True Negative: 6 \n
                        '''
