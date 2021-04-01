{
    'name': 'Test Module'
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """
test module
    """,  # Supports reStructuredText(RST) format
    'author': "Test",
    'website': "http://www.esagents.com",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented because file is not added in this example)
    'data': [
        'views/library_book.xml'
    ],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

