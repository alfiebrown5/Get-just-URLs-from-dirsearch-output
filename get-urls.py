import sys

#as dirsearch output is written in the format: status code, file size, url - we take the last option from each line.
def extract_url(line):
    parts = line.split()
    try:
    #gets all urls, ignoring top & empty lines of dirsearch output (command, empty line)
        if 'http' in parts[-1]: 
            return parts[-1]
        else:
            pass
    except IndexError:
        pass

def get_urls_from_lines(lines):
    urls = []
    for line in lines:
        url = extract_url(line)
        urls.append(url)
    #return the list without duplicates for added cleanup
    urls = list(set(urls))
    #urls = urls[:1000]
    return urls

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <dirsearch_output_file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            urls = get_urls_from_lines(lines)
            with open('urls.txt', 'w') as file:
                for url in urls:
                    if url != None:
                        file.write(f'{url}\n')
            print("URLs written to urls.txt")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()
    
