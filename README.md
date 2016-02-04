A more liberal autolink extension for python Markdown
- inspired by Django's urlize function`

Requires: http://pypi.python.org/pypi/Markdown

To make this extension loadable by Mardown, just drop ``mdx_urlize.py`` into your PYTHONPATH or projects root.

From http://stackoverflow.com/a/6553787/352452:

Once installed, you can use it in a Django template like this:

    {{ value|markdown:"urlize" }}

Or in Python code like this:

    import markdown  
    md = markdown.Markdown(safe_mode=True, extensions=['urlize'])  
    converted_text = md.convert(text)  

Here is the start of the [Markdown extension docs](http://pythonhosted.org/Markdown/extensions/index.html) in case you need more info.


