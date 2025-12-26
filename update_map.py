import re

def update_map():
    # Read the downloaded high-quality map
    with open('temp_map.svg', 'r') as f:
        svg_content = f.read()

    # Extract all path elements
    # We want to catch attributes too, so regular expression is a quick and dirty way 
    # since we know the file structure from previous cat/view_file is simple.
    # However, parsing is safer to get just string content of paths.
    # Let's simple extract everything between <svg ...> and </svg>
    # The first tag is <svg ...>
    start_tag_end = svg_content.find('>')
    end_tag_start = svg_content.rfind('</svg>')
    
    if start_tag_end == -1 or end_tag_start == -1:
        print("Could not parse temp_map.svg")
        return

    new_paths = svg_content[start_tag_end+1:end_tag_start].strip()
    
    # We need to wrap this in a group to apply transforms and class
    # The original map was roughly 250px wide centered in 500px viewbox.
    # The new map is 612px wide. To fit nicely, we scale it down.
    # Scale 0.7 brings 612 -> 428. 
    # Current viewbox is 0 0 500 600.
    # Let's try scale(0.7) and some translation to center it.
    new_map_group = f'<g class="kb-india-outline" transform="scale(0.7) translate(30, 20)">\n{new_paths}\n</g>'

    # Read index.html
    with open('index.html', 'r') as f:
        html_content = f.read()

    # Regex to find the existing path with class "kb-india-outline" (handling multiline)
    # It looks like: <path class="kb-india-outline" d="..." />
    pattern = r'<path class="kb-india-outline"\s+d="[^"]*"\s*/>'
    
    match = re.search(pattern, html_content, re.DOTALL)
    if match:
        print("Found existing map path. Replacing...")
        new_html_content = html_content[:match.start()] + new_map_group + html_content[match.end():]
        
        with open('index.html', 'w') as f:
            f.write(new_html_content)
        print("index.html updated successfully.")
    else:
        print("Could not find the target path in index.html")

if __name__ == "__main__":
    update_map()
