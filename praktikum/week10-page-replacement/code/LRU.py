def lru(pages, frames):
    memory = []
    recent = []
    page_faults = 0
    page_hits = 0

    print("\nLRU Page Replacement\n")

    for page in pages:
        if page in memory:
            page_hits += 1
            recent.remove(page)
            recent.append(page)
            print(f"Page", page ,": HIT   =",memory)
        else:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = recent.pop(0)
                memory[memory.index(lru_page)] = page
            recent.append(page)
            print(f"Page", page ,": FAULT =",memory)

    print("\nTotal Page Faults LRU :", page_faults)
    print("Total Page Hits LRU :", page_hits)

if __name__ == "__main__":
    with open("reference_string.txt") as file:
        pages = list(map(int, file.read().split(",")))

    frames = 3
    lru(pages, frames)