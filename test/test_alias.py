import unittest

import fpdf
from test.utilities import assert_pdf_equal

# python -m unittest test.test_alias


class AliasTest(unittest.TestCase):
    def test_alias_nb_pages(self):
        pdf = fpdf.FPDF()
        pdf.set_font("Times")
        pdf.add_page()
        pdf.cell(0, 10, f"Page {pdf.page_no()}/{{nb}}", align="C")
        pdf.add_page()
        pdf.cell(0, 10, f"Page {pdf.page_no()}/{{nb}}", align="C")
        assert_pdf_equal(self, pdf, "test_alias_nb_pages.pdf")

    def test_custom_alias_nb_pages(self):
        pdf = fpdf.FPDF()
        pdf.set_font("Times")
        alias = "n{}b"
        # Prerequisite to get exactly the same output in the PDF:
        # the default alias and the new one must be of same width:
        self.assertEqual(
            pdf.get_string_width(pdf.str_alias_nb_pages), pdf.get_string_width(alias)
        )
        pdf.alias_nb_pages(alias)
        pdf.add_page()
        pdf.cell(0, 10, f"Page {pdf.page_no()}/{alias}", align="C")
        pdf.add_page()
        pdf.cell(0, 10, f"Page {pdf.page_no()}/{alias}", align="C")
        assert_pdf_equal(self, pdf, "test_alias_nb_pages.pdf")
