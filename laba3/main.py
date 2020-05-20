import pdfkit


class BillTemplate(object):
    def __init__(self, filename):
        self.content = open(filename, "r").read()

    def generate(self, telephone_bill, internet_bill):
        telephone_bill = telephone_bill
        internet_bill = internet_bill
        total = telephone_bill + internet_bill

        replaces = [
            ("{{telephone_bill}}", telephone_bill),
            ("{{internet_bill}}", internet_bill),
            ("{{total}}", total),
        ]

        template = self.content
        for placeholder, value in replaces:
            template = template.replace(placeholder, str(value))

        return template


def main():
    template = BillTemplate("template.html")
    html_bill = template.generate(114.22, 7817.46)
    pdfkit.from_string(html_bill, "bill.pdf")


if __name__ == "__main__":
    main()