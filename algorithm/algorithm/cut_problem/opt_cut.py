def best_fit_decreasing(items, bin_capacity):
    # Sort items in decreasing order
    items.sort(reverse=True)

    # Initialize bins list to store the remaining capacity of each bin
    bins = [bin_capacity]

    # Initialize dictionary to keep track of which items are placed in which bin
    bin_items = {0: []}

    for item in items:
        # Find the best bin to place the item
        best_bin_index = -1
        min_remain = bin_capacity + 1
        for i, bin_remain in enumerate(bins):
            if bin_remain >= item and bin_remain - item < min_remain:
                best_bin_index = i
                min_remain = bin_remain - item

        if best_bin_index != -1:
            # Place the item in the best bin found
            bins[best_bin_index] -= item
            bin_items.setdefault(best_bin_index, []).append(item)
        else:
            # If no suitable bin found, create a new bin
            bins.append(bin_capacity - item)
            bin_items.setdefault(len(bins) - 1, []).append(item)

    return bins, bin_items


def print_solution(bins, bin_items):
    print("Number of bins required:", len(bins))
    items_num = 0

    for bin_index, items in bin_items.items():
        items_num += len(items)
        print(f"Bin {bin_index + 1}: {items}, Remaining capacity: {bins[bin_index]}")

    total_waste = sum(bins)
    print("Number of items :", items_num)
    print("\nTotal waste:", total_waste)


# Example usage
if __name__ == "__main__":
    items = [4231] * 300 + [2128] * 200 + [4128] * 200 + [1231] * 400
    bin_capacity = 15000
    print(len(items))

    bins, bin_items = best_fit_decreasing(items, bin_capacity)
    print_solution(bins, bin_items)
