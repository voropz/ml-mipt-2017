def SMAPE_scorer(estimator, X, y, deg=2.0):
    pred = estimator.predict(X)
    h = abs(pred**deg - y**deg)
    b = abs(pred**deg) + abs(y**deg)
    return -200 * sum(h / b) / y.size