{
    'name': "My Library",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Test",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '14.0.2',
    'depends': ['base'],

    'data': [
        'views/library_book.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
    
}



