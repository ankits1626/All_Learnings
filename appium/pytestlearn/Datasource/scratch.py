import html


def convert_html_to_text(html_str):
    # Convert HTML entities to their corresponding characters
    text = html.unescape(html_str)

    # Replace HTML tags with desired formatting
    text = text.replace("<p>", "\n").replace("</p>", "\n")
    text = text.replace("<ul>", "").replace("</ul>", "")
    text = text.replace("<li>", "\t•\t").replace("</li>", "\n")

    # Remove multiple consecutive newlines, then add a newline at the end
    text = '\n'.join([line for line in text.splitlines() if line.strip() != '']) + '\n'

    return text.strip('\n') + '\n'  # Ensure exactly one newline at the end


html_str = """
<p>How to Redeem:</p>
<ul>
<li>Tap redeem &amp; follow instructions on the redeemed page to use promo code.</li>
</ul>
<p>Other T&amp;Cs:</p>
<ul>
<li>Not applicable on public holidays.</li>
</ul>
"""

converted_text = convert_html_to_text(html_str)
print(repr(converted_text))