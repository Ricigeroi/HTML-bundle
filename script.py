with open('my_page.html', 'r') as html_file:
    html_content = html_file.read()

with open('style.css', 'r') as css_file:
    css_content = css_file.read()

# Embed CSS in HTML using a <style> tag
html_with_inline_css = f'<html><head><style>{css_content}</style></head><body>{html_content}</body></html>'

with open('my_page_with_inline_css.html', 'w') as output_file:
    output_file.write(html_with_inline_css)
