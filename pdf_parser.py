import os
from pdf2image import convert_from_path
from fpdf import FPDF
from PIL import Image


class PDFP:
    def __init__(self, pdf_name):
        # self.pdf_directory = os.path.join(root, 'pdfs')
        # self.img_directory = os.path.join(root, 'images')
        self.old_pdf_name = os.path.join(pdf_name)
        self.new_pdf_name = os.path.join(pdf_name[:-4] + "-corrected.pdf")
        self.pages = convert_from_path(self.old_pdf_name)
        self.cropped_pages_as_imgs = []

    def crop(self, im, page_num, split_point=0.5, write=True):
        #im = Image.open(page)
        imgwidth, imgheight = im.size
        pg_width = imgwidth - (int(imgwidth*split_point)-20)
        pg1 = (imgwidth - 2*pg_width + 20, 200, int(imgwidth*split_point), imgheight)
        pg2 = (int(imgwidth*split_point)-20, 200, imgwidth, imgheight)
        page1 = im.crop(pg1)
        page2 = im.crop(pg2)
        page1_name = os.path.join(self.img_directory, str(page_num)+'.jpg')
        page2_name = os.path.join(self.img_directory, str(page_num+1)+'.jpg')
        page1.save(page1_name)
        page2.save(page2_name)
        self.cropped_pages_as_imgs.append(page1_name)
        self.cropped_pages_as_imgs.append(page2_name)

    def make_pdf(self, cover_img_num):
        cover = Image.open(self.cropped_pages_as_imgs[cover_img_num])
        width, height = cover.size

        pdf = FPDF(unit="pt", format=[width, height])

        for page in self.cropped_pages_as_imgs:
            pdf.add_page()
            pdf.image(page, 0, 0)
        pdf.output(self.new_pdf_name, "F")

    def clean_up(self):
        for page in self.cropped_pages_as_imgs:
            os.remove(page)