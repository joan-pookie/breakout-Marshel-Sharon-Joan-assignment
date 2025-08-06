def find_needle(haystack):
    
    for i in range(len(haystack)):
        if haystack[i] == "needle":
            return "found the needle at position " + str(i)

# Example test
if __name__ == "__main__":
    data = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
    print(find_needle(data))  # Expected: found the needle at position 5
