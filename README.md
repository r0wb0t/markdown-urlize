A more liberal autolink extension for python Markdown
- inspired by Django's urlize function`

Requires: http://pypi.python.org/pypi/Markdown

To play nicely with Django, drop ``urlize.py`` into your PYTHONPATH or projects root directory as ``mdx_urlize.py`` for Django's Markup app to properly load this as an extension.

From http://stackoverflow.com/a/6553787/352452:

Once installed, you can use it in a Django template like this:

    {{ value|markdown:"urlize" }}

Or in Python code like this:

    import markdown  
    md = markdown.Markdown(safe_mode=True, extensions=['urlize:UrlizeExtension'])  
    converted_text = md.convert(text)  

Here is the start of the [Markdown extension docs](http://www.freewisdom.org/projects/python-markdown/Extensions) in case you need more info.


