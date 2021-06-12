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
