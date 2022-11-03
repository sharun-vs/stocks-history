from django.http import HttpResponse
import yfinance as yahooFinance


async def stock_view(request):
    GetFacebookInformation =  yahooFinance.Ticker("GOOGL")
    stocks_data = GetFacebookInformation.history(period="max")
    stocks_html = stocks_data.to_html()

    return HttpResponse(stocks_html)
