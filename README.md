# PDFBookSplitter

A simple program to parse pdf books where there are 2 book pages per single digital page.

Turns this:

    +----------------+-------------------+
    |                |                   |
    |                |                   |
    |        1       |         2         |      
    |                |                   |
    |                |                   |
    |                |                   |
    +----------------+-------------------+

Into this:

    +----------------+
    |                |                   
    |                |                   
    |        1       |                       
    |                |                   
    |                |                   
    |                |
    +----------------+              
    +----------------+
    |                |                   
    |                |                   
    |        2       |                       
    |                |                   
    |                |                   
    |                |
    +----------------+    