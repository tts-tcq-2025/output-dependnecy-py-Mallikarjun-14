
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

# Existing weak tests
def test_weak():
    assert(size(37) == 'S')
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    print("Weak tests passed (but may be misleading)")

# Strong test that exposes the bug
def test_strong():
    assert(size(38) == 'M'), "Expected 'M' for 38 cms, but got " + size(38)

# Run tests
test_weak()
test_strong()
