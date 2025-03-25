# test_matopeli.py

def tormaako_seinaan(x, y, leveys, korkeus):
    return x < 0 or x >= leveys or y < 0 or y >= korkeus

def tormaako_itseensa(mato_lista):
    pää = mato_lista[-1]
    return pää in mato_lista[:-1]

def test_tormaako_seinaan():
    assert tormaako_seinaan(-10, 50, 600, 400)
    assert tormaako_seinaan(600, 100, 600, 400)
    assert not tormaako_seinaan(100, 100, 600, 400)

def test_tormaako_itseensa():
    mato = [[100, 100], [110, 100], [120, 100], [130, 100], [120, 100]]
    mato2 = [[100, 100], [110, 100], [120, 100], [130, 100], [140, 100]]
    assert tormaako_itseensa(mato)
    assert not tormaako_itseensa(mato2)