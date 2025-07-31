def get_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []

    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = i * 5 + j
            color_map.append((pair_number, major, minor))
    
    return color_map

def format_color_map_entry(pair_number, major, minor):
    # Misaligned version (bug preserved)
    return f"{pair_number} | {major} | {minor}"

def print_color_map():
    color_map = get_color_map()
    for entry in color_map:
        print(format_color_map_entry(*entry))
    return len(color_map)

# Weak test: only counts the rows
def test_row_count():
    result = print_color_map()
    assert(result == 25)
    print("Row count test passed (but formatting might still be wrong)")

# Strong test: checks formatting
def test_formatting():
    entry = format_color_map_entry(0, "White", "Blue")
    expected = " 0 | White | Blue"  # This is just an example of aligned format
    assert entry == expected, f"Expected formatted line:\n'{expected}'\nBut got:\n'{entry}'"

# Run tests
test_row_count()
test_formatting()
