doctest — Testing Through Documentation

Purpose:	Write automated tests as part of the documentation for a module.

doctest tests source code by running examples embedded in the documentation and verifying that they produce the expected results. It works by parsing the help text to find examples, running them, then comparing the output text against the expected value. Many developers find doctest easier to use than unittest because, in its simplest form, there is no API to learn before using it. However, as the examples become more complex the lack of fixture management can make writing doctest tests more cumbersome than using unittest.

Python Test Cases

Allowed editors: vi, vim, emacs

All your files should end with a new line

All your test files should be inside a folder tests

All your test files should be text files (extension: .txt)

All your tests should be executed by using this command: python3 -m doctest ./tests/*

All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')

All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')

A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
