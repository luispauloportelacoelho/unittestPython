from behave import step

from calc import sum_values



@step('Sum "{value_0}" with "{value_1}"')
def test_sum(context, value_0, value_1):
    context.result = float(sum_values(float(value_0), float(value_1)))


@step('the result is "{result_operation}"')
def test_sum_resutl(context, result_operation):
    assert context.result == float(result_operation)
