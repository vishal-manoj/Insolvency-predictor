import os.path

import pandas as pd
from fpdf import FPDF
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

        self.gp_margin = self.gross_profit / self.revenue_from_operations if self.revenue_from_operations != 0 else 0

        self.operating_profit_ratio = self.operating_income / self.revenue_from_operations \
            if self.revenue_from_operations != 0 else 0

        self.operating_exp_ratio = self.operating_income / self.revenue_from_operations \
            if self.revenue_from_operations != 0 else 0

        self.cash_flow_rate = self.operating_cash_flow / self.current_liability if self.current_liability != 0 else 0
        self.debt_equity_ratio = self.long_term_debt / self.equity_capital if self.equity_capital != 0 else 0
        self.cash_flow_per_share = self.cash_flow / self.no_of_shares if self.no_of_shares != 0 else 0
        self.revenue_per_share = self.revenue_from_operations / self.no_of_shares if self.no_of_shares != 0 else 0
        self.operating_profit_per_share = self.operating_income / self.no_of_shares if self.no_of_shares != 0 else 0
        self.pretax_income_per_share = self.pbt / self.no_of_shares if self.no_of_shares != 0 else 0
        self.current_ratio = self.current_asset / self.current_liability if self.current_liability != 0 else 0

        self.quick_ratio = (self.cash_cash_equivalents + self.marketable_securities +
                            self.trade_receivables) / self.current_liability if self.current_liability != 0 else 0

        self.interest_expense_ratio = self.finance_cost / (self.revenue_from_operations + self.other_income) \
            if (self.revenue_from_operations + self.other_income) != 0 else 0

        self.networth_asset_ratio = self.equity_capital / self.total_asset if self.total_asset != 0 else 0

        self.long_term_fund_suitability = (self.long_term_debt + self.equity_capital) / (self.total_asset -
                                                                                         self.current_asset) \
            if (self.total_asset - self.current_liability) != 0 else 0

        self.contingent_liability_networth = self.contingent_liability / self.equity_capital \
            if self.equity_capital != 0 else 0

        self.inventory_receivables_equity = (self.inventory + self.trade_receivables) / self.equity_capital \
            if self.equity_capital != 0 else 0

        self.asset_turnover_ratio = self.revenue_from_operations / self.total_asset if self.total_asset != 0 else 0

        self.trade_receivables_turnover = self.credit_sales / self.trade_receivables \
            if self.trade_receivables != 0 else 0

        self.avg_collection_days = self.trade_receivables_turnover / 365
        self.inventory_turnover = self.cost_goods_sold / self.inventory if self.inventory != 0 else 0

        self.working_capital_total_asset_ratio = (self.current_asset - self.current_liability) / self.total_asset \
            if self.total_asset != 0 else 0

        self.quick_asset_total_asset_ratio = (self.cash_cash_equivalents + self.marketable_securities +
                                              self.trade_receivables) / self.total_asset if self.total_asset != 0 else 0

        self.current_asset_total_asset_ratio = self.current_asset / self.total_asset if self.total_asset != 0 else 0

        self.cash_asset_total_asset_ratio = self.cash_cash_equivalents / self.total_asset \
            if self.total_asset != 0 else 0

        self.cash_current_liability_ratio = self.cash_cash_equivalents / self.current_liability \
            if self.current_liability != 0 else 0

        self.inventory_working_capital_ratio = self.inventory / (self.current_asset + self.current_liability) \
            if (self.current_asset + self.current_liability) != 0 else 0

        self.inventory_current_liability_ratio = self.inventory / self.current_liability \
            if self.current_liability != 0 else 0

        self.working_capital_equity_ratio = (self.current_asset + self.current_liability) / self.equity_capital \
            if self.equity_capital != 0 else 0

        self.current_liability_equity_ratio = self.current_liability / self.equity_capital \
            if self.equity_capital != 0 else 0

        self.retained_earnings_total_asset = self.retained_earnings / self.total_asset if self.total_asset != 0 else 0
        self.total_income_exp_ratio = self.total_income / self.total_expense if self.total_expense != 0 else 0
        self.total_exp_asset_ratio = self.total_expense / self.total_asset if self.total_asset != 0 else 0

        self.current_asset_turnover = self.current_asset / self.revenue_from_operations \
            if self.revenue_from_operations != 0 else 0

        self.quick_asset_turnover = (self.cash_cash_equivalents + self.marketable_securities +
                                     self.trade_receivables) / self.revenue_from_operations \
            if self.revenue_from_operations != 0 else 0

        self.working_capital_turnover = (self.current_asset - self.current_liability) / self.revenue_from_operations \
            if self.revenue_from_operations != 0 else 0

        self.cash_turnover = self.cash_cash_equivalents / self.revenue_from_operations  \
            if self.revenue_from_operations != 0 else 0

        self.cashflow_sales_ratio = self.cash_flow / self.revenue_from_operations  \
            if self.revenue_from_operations != 0 else 0

        self.cashflow_asset_ratio = self.cash_flow / self.total_asset if self.total_asset != 0 else 0
        self.cfo_asset_ratio = self.operating_cash_flow / self.total_asset if self.total_asset != 0 else 0
        self.cashflow_equity_ratio = self.cash_flow / self.equity_capital if self.equity_capital != 0 else 0
        self.net_income_total_asset_ratio = self.net_profit / self.total_asset if self.total_asset != 0 else 0
        self.interest_coverage_ratio = self.finance_cost / self.ebit if self.ebit != 0 else 0

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
        self.model = joblib.load('insolvency_prediction_model.pkl')
        self.insolvency_prediction = self.model.predict(self.data)

    def generate_report(self):
        if self.insolvency_prediction == 0:
            self.insolvency_report = f''' 
            \t\t\t\t\t\t INSOLVENCY REPORT OF {self.company_name}
        \n  
        On the basis of the financial data of {self.company_name} for the year {self.year},
        it has been predicted that the company will not become insolvent. The prediction has been made
        on the basis of the machine learning model Random Forest Classifier.
                
        Details of the machine Learning model:
        
        For predicting whether the company will become insolvent or not Machine Learning model named 
        Random Forest Classifier has been used. The model has been trained on 43 ratios of 6819
        companies.
                        
        Source of data for training Machine Learning model: Kaggle
                        
        Accuracy of Model:\t\t\t\t 0.97
        True Positives:\t\t\t\t 1312
        False Positives:\t\t\t\t 1
        False Negative:\t\t\t\t 45
        True Negative:\t\t\t\t 6
        
        Financial Ratios:
        
        Operating Gross Margin:\t\t\t\t\t\t\t\t{self.gp_margin}
        Operating Profit Rate:\t\t\t\t\t\t\t\t{self.operating_profit_ratio}
        Operating Expense Rate:\t\t\t\t\t\t\t\t{self.operating_exp_ratio} 
        Cash flow rate:\t\t\t\t\t\t\t\t{self.cash_flow_rate}
        Debt-Equity Ratio:\t\t\t\t\t\t\t\t{self.debt_equity_ratio}
        Cash Flow Per Share:\t\t\t\t\t\t\t\t{self.cash_flow_per_share}
        Revenue Per Share:\t\t\t\t\t\t\t\t{self.revenue_per_share}   
        Operating Profit Per Share:\t\t\t\t\t\t\t\t{self.operating_profit_per_share}
        Pre-tax Income Per Share:\t\t\t\t\t\t\t\t{self.pretax_income_per_share}
        Current Ratio:\t\t\t\t\t\t\t\t{self.current_ratio}
        Quick Ratio:\t\t\t\t\t\t\t\t{self.quick_ratio}
        Interest Expense Ratio:\t\t\t\t\t\t\t\t{self.interest_expense_ratio}
        Net worth/Assets:\t\t\t\t\t\t\t\t{self.networth_asset_ratio}
        Long-term fund suitability ratio:\t\t\t\t\t\t\t\t{self.long_term_fund_suitability}
        Contingent liabilities/Net worth:\t\t\t\t\t\t\t\t{self.contingent_liability}
        Inventory and accounts receivable/Net value:\t\t\t\t\t\t\t\t{self.inventory_receivables_equity}
        Total Asset Turnover:\t\t\t\t\t\t\t\t{self.asset_turnover_ratio}
        Accounts Receivable Turnover:\t\t\t\t\t\t\t\t{self.trade_receivables_turnover}
        Average Collection Days:\t\t\t\t\t\t\t\t{self.avg_collection_days}
        Inventory Turnover Rate (times):\t\t\t\t\t\t\t\t{self.inventory_turnover}
        Working Capital to Total Assets:\t\t\t\t\t\t\t\t{self.working_capital_total_asset_ratio}
        Quick Assets/Total Assets:\t\t\t\t\t\t\t\t{self.quick_asset_total_asset_ratio}
        Current Assets/Total Assets:\t\t\t\t\t\t\t\t{self.current_asset_total_asset_ratio} 
        Cash/Total Assets:\t\t\t\t\t\t\t\t{self.cash_asset_total_asset_ratio}
        Cash/Current Liability:\t\t\t\t\t\t\t\t{self.cash_current_liability_ratio}
        Inventory/Working Capital:\t\t\t\t\t\t\t\t{self.inventory_working_capital_ratio}
        Inventory/Current Liability:\t\t\t\t\t\t\t\t{self.inventory_current_liability_ratio}
        Working Capital/Equity:\t\t\t\t\t\t\t\t{self.working_capital_equity_ratio}
        Current Liabilities/Equity:\t\t\t\t\t\t\t\t{self.current_liability_equity_ratio}
        Retained Earnings to Total Assets:\t\t\t\t\t\t\t\t{self.retained_earnings}
        Total income/Total expense:\t\t\t\t\t\t\t\t{self.total_income_exp_ratio} 
        Total expense/Assets:\t\t\t\t\t\t\t\t{self.total_exp_asset_ratio}
        Current Asset Turnover Rate:\t\t\t\t\t\t\t\t{self.current_asset_turnover} 
        Quick Asset Turnover Rate:\t\t\t\t\t\t\t\t{self.quick_asset_turnover}
        Working capital Turnover Rate:\t\t\t\t\t\t\t\t{self.working_capital_turnover} 
        Cash Turnover Rate:\t\t\t\t\t\t\t\t{self.cash_turnover}
        Cash Flow to Sales:\t\t\t\t\t\t\t\t{self.cashflow_sales_ratio}
        Cash Flow to Total Assets:\t\t\t\t\t\t\t\t{self.cashflow_asset_ratio}
        CFO to Assets:\t\t\t\t\t\t\t\t{self.cfo_asset_ratio}
        Cash Flow to Equity:\t\t\t\t\t\t\t\t{self.cashflow_equity_ratio}
        Net Income to Total Assets:\t\t\t\t\t\t\t\t{self.net_income_total_asset_ratio}
        Interest Coverage Ratio (Interest expense to EBIT):\t\t\t\t\t\t\t\t{self.interest_coverage_ratio}
        '''

        if self.insolvency_prediction == 1:
            self.insolvency_report = f''' 
            \t\t\t\t\t\t INSOLVENCY REPORT OF {self.company_name}
        \n
        On the basis of the financial data of {self.company_name} for the year {self.year}, 
        it has been predicted that the company will become insolvent. The prediction has been made 
        on the basis of the machine learning model Random Forest Classifier.

        Details of the machine Learning model:
        
        For predicting whether the company will become insolvent or not Machine Learning model named
        Random Forest Classifier has been used. The model has been trained on 43 ratios of 6819
        companies.
                        
        Source of data for training Machine Learning model: Kaggle
                        
        Accuracy of Model:\t\t\t\t 0.97
        True Positives:\t\t\t\t 1312
        False Positives:\t\t\t\t 1
        False Negative:\t\t\t\t 45
        True Negative:\t\t\t\t 6
        
        Financial Ratios:
        
        Operating Gross Margin:\t\t\t\t\t\t\t\t{self.gp_margin}
        Operating Profit Rate:\t\t\t\t\t\t\t\t{self.operating_profit_ratio}
        Operating Expense Rate:\t\t\t\t\t\t\t\t{self.operating_exp_ratio} 
        Cash flow rate:\t\t\t\t\t\t\t\t{self.cash_flow_rate}
        Debt-Equity Ratio:\t\t\t\t\t\t\t\t{self.debt_equity_ratio}
        Cash Flow Per Share:\t\t\t\t\t\t\t\t{self.cash_flow_per_share}
        Revenue Per Share:\t\t\t\t\t\t\t\t{self.revenue_per_share}   
        Operating Profit Per Share:\t\t\t\t\t\t\t\t{self.operating_profit_per_share}
        Pre-tax Income Per Share:\t\t\t\t\t\t\t\t{self.pretax_income_per_share}
        Current Ratio:\t\t\t\t\t\t\t\t{self.current_ratio}
        Quick Ratio:\t\t\t\t\t\t\t\t{self.quick_ratio}
        Interest Expense Ratio:\t\t\t\t\t\t\t\t{self.interest_expense_ratio}
        Net worth/Assets:\t\t\t\t\t\t\t\t{self.networth_asset_ratio}
        Long-term fund suitability ratio:\t\t\t\t\t\t\t\t{self.long_term_fund_suitability}
        Contingent liabilities/Net worth:\t\t\t\t\t\t\t\t{self.contingent_liability}
        Inventory and accounts receivable/Net value:\t\t\t\t\t\t\t\t{self.inventory_receivables_equity}
        Total Asset Turnover:\t\t\t\t\t\t\t\t{self.asset_turnover_ratio}
        Accounts Receivable Turnover:\t\t\t\t\t\t\t\t{self.trade_receivables_turnover}
        Average Collection Days:\t\t\t\t\t\t\t\t{self.avg_collection_days}
        Inventory Turnover Rate (times):\t\t\t\t\t\t\t\t{self.inventory_turnover}
        Working Capital to Total Assets:\t\t\t\t\t\t\t\t{self.working_capital_total_asset_ratio}
        Quick Assets/Total Assets:\t\t\t\t\t\t\t\t{self.quick_asset_total_asset_ratio}
        Current Assets/Total Assets:\t\t\t\t\t\t\t\t{self.current_asset_total_asset_ratio} 
        Cash/Total Assets:\t\t\t\t\t\t\t\t{self.cash_asset_total_asset_ratio}
        Cash/Current Liability:\t\t\t\t\t\t\t\t{self.cash_current_liability_ratio}
        Inventory/Working Capital:\t\t\t\t\t\t\t\t{self.inventory_working_capital_ratio}
        Inventory/Current Liability:\t\t\t\t\t\t\t\t{self.inventory_current_liability_ratio}
        Working Capital/Equity:\t\t\t\t\t\t\t\t{self.working_capital_equity_ratio}
        Current Liabilities/Equity:\t\t\t\t\t\t\t\t{self.current_liability_equity_ratio}
        Retained Earnings to Total Assets:\t\t\t\t\t\t\t\t{self.retained_earnings}
        Total income/Total expense:\t\t\t\t\t\t\t\t{self.total_income_exp_ratio} 
        Total expense/Assets:\t\t\t\t\t\t\t\t{self.total_exp_asset_ratio}
        Current Asset Turnover Rate:\t\t\t\t\t\t\t\t{self.current_asset_turnover} 
        Quick Asset Turnover Rate:\t\t\t\t\t\t\t\t{self.quick_asset_turnover}
        Working capital Turnover Rate:\t\t\t\t\t\t\t\t{self.working_capital_turnover} 
        Cash Turnover Rate:\t\t\t\t\t\t\t\t{self.cash_turnover}
        Cash Flow to Sales:\t\t\t\t\t\t\t\t{self.cashflow_sales_ratio}
        Cash Flow to Total Assets:\t\t\t\t\t\t\t\t{self.cashflow_asset_ratio}
        CFO to Assets:\t\t\t\t\t\t\t\t{self.cfo_asset_ratio}
        Cash Flow to Equity:\t\t\t\t\t\t\t\t{self.cashflow_equity_ratio}
        Net Income to Total Assets:\t\t\t\t\t\t\t\t{self.net_income_total_asset_ratio}
        Interest Coverage Ratio (Interest expense to EBIT):\t\t\t\t\t\t\t\t{self.interest_coverage_ratio}
        '''


class ReportGenerator:
    def __init__(self, path, report_data, company):
        self.path = path
        self.report_data = report_data
        self.pdf_report = None
        self.company = company

    def save(self):
        self.pdf_report = FPDF()
        self.pdf_report.add_page()
        self.pdf_report.set_font('Arial', size=12)
        self.pdf_report.set_margins(left=0.5, top=1, right=1)
        self.pdf_report.multi_cell(0, 10, self.report_data)
        self.pdf_report.output(os.path.join(self.path, 'Insolvency Prediction Report.pdf'))
