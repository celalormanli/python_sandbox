from src.regular_expressions import RegularExpressions


def test_find_emails():
    regular_expressions = RegularExpressions()
    assert regular_expressions.find_emails(
        'fsbvbfds dfsvfds test@emailcom fdvfd fjsı ıfşslfhlkvh fdlkvh şdfhvjdsfkhk test@test.net') == ['test@test.net']


def test_validete_email():
    regular_expressions = RegularExpressions()
    assert regular_expressions.validete_email('test@test.net')
    assert regular_expressions.validete_email('test@emailcom') == False
