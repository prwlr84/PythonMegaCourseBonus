import pandas as pd
from fpdf import FPDF

df = pd.read_csv('articles.csv', dtype={'id': str})


class Article:
    def __init__(self, a_id):
        self.a_id = a_id
        self.name = df.loc[df['id'] == self.a_id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.a_id, 'price'].squeeze()

    def sell(self):
        df.loc[df['id'] == self.a_id, 'in stock'] -= 1
        df.to_csv('articles.csv', index=False)

    def is_on_stock(self):
        return df.loc[df['id'] == self.a_id, 'in stock'].squeeze()


class Invoice:
    def __init__(self, c_name, article_obj):
        self.name = c_name
        self.article = article_obj

    def create_invoice(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.1", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Customer: {self.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)
selected = input('Select article:')
article = Article(selected)
if article.is_on_stock():
    customer = input('Add your company:')
    article.sell()
    inv = Invoice(customer, article)
    inv.create_invoice()

if __name__ == '__main__':
    print('PyCharm')
