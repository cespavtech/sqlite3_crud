"""
==============================================================================
==============================Tabs Choices====================================

******************************************************************************

All Tabs choices

******************************************************************************

User selected choices will be matched with this one and function will be called
In the choice_functions module, The boot method will be called for the file with 
prefix '_func_' + name of the file module
[ e.g. "func_1": "update_students" ] will lead to calling of _func_update_students.boot(choice)

If no matching choice found!
Invalid comand error will be displayed and the user will repeat the previous action
Previous window will be loaded, unless the user gets back by
Entering 0 or visits the homepage via 00

==============================================================================

"""