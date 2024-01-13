from project import get_critical_points, get_x_intercepts, analyze
import sympy as sp

def test_get_critical_points():
    x = sp.Symbol('x')

    expr = sp.sympify("x")
    assert get_critical_points(expr, sp.diff(expr, x), x) == []

    expr = sp.sympify("x^2")
    assert get_critical_points(expr, sp.diff(expr, x), x) == [{'x': '0', 'y': '0', "type": "Min"}]

    expr = sp.sympify("10/(x-5)")
    assert get_critical_points(expr, sp.diff(expr, x), x) == []

    expr = sp.sympify("(x-10)^2/(2*x)")
    assert get_critical_points(expr, sp.diff(expr, x), x) == [{'x': '-10', 'y': '-20', "type": "Max"}, {'x': '10', 'y': '0', "type": "Min"}]

def test_get_x_intercepts():
    x = sp.Symbol('x')

    expr = sp.sympify("x")
    assert get_x_intercepts(expr, x) == [{'x': '0', 'y': '0'}]

    expr = sp.sympify("x^2")
    assert get_x_intercepts(expr, x) == [{'x': '0', 'y': '0'}]

    expr = sp.sympify("10/(x-5)")
    assert get_x_intercepts(expr, x) == []

    expr = sp.sympify("(x-10)^2/(2*x)")
    assert get_x_intercepts(expr, x) == [{'x': '10', 'y': '0'}]


def test_analyze():
    assert analyze("x") == {
                                "equation": sp.sympify('x'),
                                "left_limit": -sp.oo,
                                "right_limit": sp.oo,
                                "deriv": 1,
                                "critical_points": [],
                                "x_intercepts": [{'x': '0', 'y': '0'}],
                                "y_intercept": {'x': '0', 'y': '0'}
                            }
    assert analyze("x^2") == {
                                        "equation": sp.sympify('x^2'),
                                        "left_limit": sp.oo,
                                        "right_limit": sp.oo,
                                        "deriv": sp.sympify("2*x"),
                                        "critical_points": [{'x': '0', 'y': '0', "type": "Min"}],
                                        "x_intercepts": [{'x': '0', 'y': '0'}],
                                        "y_intercept": {'x': '0', 'y': '0'}
                                    }
    assert analyze("10/(x-5)") == {
                                        "equation": sp.sympify('10/(x-5)'),
                                        "left_limit": -sp.sympify(0),
                                        "right_limit": sp.sympify(0),
                                        "deriv": sp.sympify("-10/(x-5)^2"),
                                        "critical_points": [],
                                        "x_intercepts": [],
                                        "y_intercept": {'x': '0', 'y': '-2'}
                                    }
    assert analyze("(x-10)^2/(2*x)") == {
                                            "equation": sp.sympify('(x-10)^2/(2*x)'),
                                            "left_limit": -sp.oo,
                                            "right_limit": sp.oo,
                                            "deriv": sp.sympify("(2*x - 20)/(2*x) - (x - 10)^2/(2*x^2)"),
                                            "critical_points": [{'x': '-10', 'y': '-20', 'type': 'Max'}, {'x': '10', 'y': '0', 'type': 'Min'}],
                                            "x_intercepts": [{'x': '10', 'y': '0'}],
                                            "y_intercept": {'x': '0', 'y': 'zoo'}
                                        }