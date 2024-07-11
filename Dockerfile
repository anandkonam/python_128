FROM python
COPY .  c:\python_programs
cmd ["python", "c:\python_programs/str_fun_demo.py"]