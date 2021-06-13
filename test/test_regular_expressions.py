from src.regular_expressions import RegularExpressions


def test_find_emails():
    regular_expressions = RegularExpressions()
    assert regular_expressions.find_emails(
        'fsbvbfds dfsvfds test@emailcom fdvfd fjsı ıfşslfhlkvh fdlkvh şdfhvjdsfkhk test@test.net') == ['test@test.net']


def test_validete_email():
    regular_expressions = RegularExpressions()
    assert regular_expressions.validete_email('test@test.net')
    assert regular_expressions.validete_email('test@emailcom') == False


def test_find_numbers():
    regular_expressions = RegularExpressions()
    assert regular_expressions.find_numbers(
        'dskhjvadsl kjsşakjfşaksljdflşksajşfk jadsşlkfj  asd 76868 fksdljfkl  4654665') == ['76868', '4654665']


def test_find_senders():
    regular_expressions = RegularExpressions()
    assert regular_expressions.find_senders(
        'gsdklgdsj lk jdsşlk Sender test sender Recievers dsfjdslkfjşdslk') == ['test sender']


def test_find_amounts():
    regular_expressions = RegularExpressions()
    assert regular_expressions.find_amounts(
        'dskhjvadsl kjsşak125$jfşaksljdflşksajşfk jadsşlkfj  asd 76868 fksdljfkl  50$ 4654665') == ['125$', '50$']


def test_find_plate_numbers():
    regular_expressions = RegularExpressions()
    assert regular_expressions.find_plate_numbers(
        'dskhjvadsl kjsşakjfşaks73AS585l73jdflşksajşfk jadsşlkfj  asd 53225358 dasdsdas 04 SL 945 jdslkjflsd') == ['73AS585', '04 SL 945']
