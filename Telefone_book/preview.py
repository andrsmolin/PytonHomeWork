from cgitb import html
from tkinter.ttk import Style
import modul_use_telefone_book as mt
from modul_use_telefone_book import return_data


def create():
    style = "style = 'font-size: 22px;'"
    html = '<html>\n <head></head>\n <body>\n'
    html += ' <p{}> {} </p>\n' \
        .format(style, mt.return_data())
    html += ' </body >\n </html>'

    with open('tel.html', 'w') as page:
        page.write(html)
    return html
