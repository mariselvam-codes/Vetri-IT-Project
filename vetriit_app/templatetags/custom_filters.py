from django import template
import re
register = template.Library()

@register.filter(name='regex_sub')
def regex_sub(value, args):
    """
    Usage: {{ value|regex_sub:"pattern,replacement" }}
    Example: {{ "123-456"|regex_sub:"\\D," }}  -> "123456"
    """
    try:
        pattern, repl = args.split(',', 1)
    except ValueError:
        return value  # incorrect usage
    return re.sub(pattern, repl, value)

@register.filter
def digits_only(value):
    """Remove all non-digit characters."""
    if not value:
        return ''
    return re.sub(r'\D', '', value)

@register.filter
def colorize_green(text):
    return f'<span style="color:#0A933C;">{text}</span>'

@register.filter
def color_black(value):
    return f'<span style="color: #000000;">{value}</span>'

@register.filter
def color_green(value):
    return f'<span style="color: #0a933c;">{value}</span>'

@register.filter
def heading_color(value):
    """
    Returns HTML where first word is black and the rest is green (#0A933C).
    Use with |safe in template.
    """
    if not value:
        return ""
    parts = str(value).split()
    if len(parts) == 1:
        return f"<span style='color:#0A933C'>{parts[0]}</span>"
    first = parts[0]
    rest = " ".join(parts[1:])
    return f"<span style='color:#0A933C'>{first}</span> <span style='color:#000000'>{rest}</span>"

@register.filter
def split_alternate(value):
    if not value:
        return ""

    words = value.split()
    formatted_text = ""

    for index, word in enumerate(words):
        if (index + 1) % 2 == 1:
            formatted_text += f"<span style='color:#000000'>{word}</span> "
        else:
            formatted_text += f"<span style='color:#0A933C'>{word}</span> "

    return formatted_text.strip()

@register.filter
def split_first(value):
    if not value:
        return ["", ""]
    parts = value.split(" ", 1)
    if len(parts) > 1:
        return parts
    return [value, ""]


@register.filter
def alternate_color(value):
    if not value:
        return ""

    words = value.split()
    formatted_text = ""

    for index, word in enumerate(words):
        if (index + 1) % 2 == 1:  # ODD
            formatted_text += f"<span style='color:#0A933C'>{word}</span> "
        else:  # EVEN
            formatted_text += f"<span style='color:#000000'>{word}</span> "

    return formatted_text.strip()

@register.filter
def half_color(text):
    words = text.split()
    half = len(words) // 2
    first = " ".join(words[:half])
    second = " ".join(words[half:])
    return f'<span style="color:#000;">{first}</span> <span style="color:#0A933C;">{second}</span>'

@register.filter
def color_words(value):
    words = value.split()
    colored_words = []

    for i, word in enumerate(words):
        if i % 2 == 0:
            colored_words.append(f'<span style="color:#000000;">{word}</span>')
        else:
            colored_words.append(f'<span style="color:#0A933C;">{word}</span>')
    
    return " ".join(colored_words)

@register.filter
def colorize_25_50_25(text):
    words = text.split()
    if not words:
        return text
    n = len(words)
    first = int(n * 0.25)
    middle = int(n * 0.5)
    last = n - (first + middle)

    first_part = " ".join(words[:first])
    middle_part = " ".join(words[first:first+middle])
    last_part = " ".join(words[first+middle:])

    return (
        f"<span style='color:#000000;'>{first_part}</span> "
        f"<span style='color:#0A933C;'>{middle_part}</span> "
        f"<span style='color:#000000;'>{last_part}</span>"
    )

@register.filter
def color_title_one(value):
    """Makes title_one text green (#0A933C)."""
    if not value:
        return ""
    return f"<span style='color:#0A933C;'>{value}</span>"

@register.filter
def color_title_two(value):
    """Makes title_two text black (#000000)."""
    if not value:
        return ""
    return f"<span style='color:#000000;'>{value}</span>"