"""Calculates linear regression slope and intercept."""
def linear_regression(x, y):
    n = len(x)
    m_x, m_y = sum(x)/n, sum(y)/n
    SS_xy = sum([xi*yi for xi, yi in zip(x, y)]) - n*m_x*m_y
    SS_xx = sum([xi*xi for xi in x]) - n*m_x*m_x
    b1 = SS_xy / SS_xx; b0 = m_y - b1*m_x
    return b0, b1
