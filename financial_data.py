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
        self.contingent_liability = kwargs.get('ca')
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
        self.gross_profit = self.revenue_from_operations-self.cost_goods_sold
        self.total_income = self.revenue_from_operations + self.other_income
        self.total_expense = self.cost_goods_sold + self.operating_expenses + self.finance_cost + self.tax_amount
        self.net_profit = self.total_income - self.total_expense
        self.operating_income = self.total_income - (self.cost_goods_sold + self.operating_expenses)
        self.pbt = self.revenue_from_operations - (self.cost_goods_sold + self.operating_expenses + self.finance_cost)

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
        

