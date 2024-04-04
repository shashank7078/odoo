{
    "name": "School",
    "version": "0.1",
    "depends": ["base"],
    "author": "Silvestar",
    "category": "Education",
    "description": "This module created for schools to manage student and teachers.",
    "data":[
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/image_views.xml',
        # 'views/sections_views.xml',
        'views/menuitem.xml',

    ],
    "installable": True,
    "application": True,
}
