class FinancialData:
    def __init__(self, **kwargs):
        self.company_name = kwargs.get('name')
        self.year = kwargs.get('year')
        self.no_of_shares = kwargs.get('no_of_shares')
        self.revenue_from_operations = kwargs.get('rfo')
        self.credit_sales = kwargs.get('credit_sales')
        self.other_income = kwargs.get('oi')
        self.depreciation_amortization = kwargs.get('da')
        self.cost_goods_sold = kwargs.get('cgs')
        self.operating_expenses = kwargs.get('oex')
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
