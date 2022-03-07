{'name': 'Rocker Reporting Application v3',
 'summary': 'Linux/Unix/Windows version. Collect data from various datasources to Excel or Powerpoint. Create report and present business graphs with Excel or generate Powerpoint slide decks',
 'description': 'Get data from Odoo & external PostgreSQL, SQLServer, MySQL, MariaDB, ODBC or Oracle databases.',
 'author': 'Antti Kärki',
 'depends': ['base','web','mail'],
 'license': 'AGPL-3',
 'category': 'Extra Tools',
 'version': '15.0.3.0.1',
 'data': [
  'security/rocker_security.xml',
  'security/ir.model.access.csv',
    'views/database_view.xml',
    'views/archive_view.xml',
     'views/report_view.xml',
     'views/executor_view.xml',
     'views/rocker_about.xml',
     'wizard/rocker_popup_wizard.xml',
     'data/rocker_data.xml',
     'views/rocker_menu.xml',
 ],
 'application': True,
 'installable': True,
 'images': ['static/description/main_screenshot.png'],

 }
