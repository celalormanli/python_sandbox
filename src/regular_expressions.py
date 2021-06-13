import re


class RegularExpressions:
    def find_emails(self, input_text):
        regex = r'\S+@\S+\.\S+'
        return re.findall(regex, input_text)

    def validete_email(self, input_text):
        regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if re.search(regex, input_text):
            return True
        return False

    def find_numbers(self, input_text):
        regex = r'\d+'
        return re.findall(regex, input_text)

    def find_senders(self, input_text):
        regex = r'Sender (.*) Recievers'
        return re.findall(regex, input_text)

    def find_amounts(self, input_text):
        regex = r'[0-9]+\$'
        return re.findall(regex, input_text)

    def find_amounts(self, input_text):
        regex = r'[0-9]+\$'
        return re.findall(regex, input_text)

    def find_plate_numbers(self, input_text):
        regex = r'\d{2}\s?\S{1,3}[A-Z]\s?\d{2,4}'
        return re.findall(regex, input_text)
