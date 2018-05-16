from behave import step

from calc import sum_values

result = None

@step('Sum "{value_0:d}" with "{value_1:d}"')
def test_sum(context, value_0, value_1):
    global result
    result = sum_values(value_0, value_1)


@step('the result is "{result_operation:d}"')
def test_sum_resutl(context, result_operation):
    assert result == result_operation
