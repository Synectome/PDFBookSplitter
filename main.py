import os
from pdf_parser import PDFP

if __name__=="__main__":
    print('here we go')
    cwd = os.getcwd()
    document = PDFP(cwd, 'otake-hideo-opening-theory-made-easy.pdf')
    page_num = 0
    for page in document.pages:
        print(page_num)
        document.crop(page, page_num, split_point=0.6)
        page_num+=2

    document.make_pdf(1)
    document.clean_up()
