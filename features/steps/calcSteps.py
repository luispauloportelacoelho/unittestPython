from behave import step
from calc import sum_values

result


@step('Sum "{value_0}" com "{value_1}"')
def test_sum(context, value_0, value_1):
    global result
    result = sum_values(value_0, value_1)


@step('the result is "{result_operation}"')
def test_sum_resutl(complex, result_operation):
    assert result == result_operation
