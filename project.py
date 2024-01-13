import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def main():
    equation = input('f(x) = ')
    eqt_nlz = analyze(equation)
    show_equation(eqt_nlz["equation"], convert(eqt_nlz))
    

def get_critical_points(expr, deriv, x):
    sec_deriv_ = sp.diff(deriv, x)
    critical_points = []
    critical_points_ = sp.solve(deriv, x)
    for point in critical_points_:
        if sec_deriv_.subs(x, point) < 0:
            st = 'Max'     
        elif sec_deriv_.subs(x, point) > 0:
            st = 'Min'
        else:
            continue
        critical_points.append({
            'x': sp.pretty(point),
            'y': sp.pretty(expr.subs(x, point)),
            'type': st
        })
    return critical_points
def get_x_intercepts(expr, x):
    x_intercepts = []
    x_intercepts_ = sp.solveset(expr, x)
    for point in x_intercepts_:
        x_intercepts.append({
            'x': sp.pretty(point),
            'y': '0'
        })
    return x_intercepts

def analyze(equation):
    x = sp.Symbol('x')
    expr = sp.sympify(equation)
    left_limit = sp.limit(expr, x, -sp.oo)
    right_limit = sp.limit(expr, x, sp.oo)
    deriv = sp.diff(expr, x)
    critical_points = get_critical_points(expr, deriv, x)
    x_intercepts = get_x_intercepts(expr, x)
    y_intercept = {
        'x': '0',
        'y': sp.pretty(expr.subs(x, 0))
    }

    return {
        "equation": expr,
        "left_limit": left_limit,
        "right_limit": right_limit,
        "deriv": deriv,
        "critical_points": critical_points,
        "x_intercepts": x_intercepts,
        "y_intercept": y_intercept
    }
def convert(data):
    st = f'Function: \n{str(sp.pretty(data["equation"]))}\nDerivative:\n{str(sp.pretty(data["deriv"]))}\nLeft limit: {data["left_limit"]}\nRight limit: {data["right_limit"]}\n'

    st += "\nY-intercept: "
    if not data["y_intercept"]:
        st += "Y-intercept: None"
    else:
        st += f'({data["y_intercept"]["x"]}, 0)'

    st += "\nX-intercepts: "
    if not data["x_intercepts"]:
        st += "None"
    else: 
        for point in data["x_intercepts"]:
            st += f'(0, {point["y"]})\n'
    
    st += "\nCritical points: "
    if not data["critical_points"]:
        st += "None"
    else:
        for point in data["critical_points"]:
            st += f'({point["x"]}, {point["y"]}) - {point["type"]}\n'
    return st

def show_equation(expr, data):
    x = np.linspace(-10, 10, 250)

    _, ax = plt.subplots(1, 1, figsize=(8, 4))

    ax.grid(True, which='both')

    ax.spines['left'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()

    ax.spines['bottom'].set_position('zero')

    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    props = dict(boxstyle='round', facecolor='grey', alpha=0.15)  # bbox features
    ax.text(1.03, 0.98, data, transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=props)

    plt.tight_layout()

    plt.plot(x, eval(str(expr)))
    plt.show()

if __name__ == '__main__':
    main()

