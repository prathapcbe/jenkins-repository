FROM python:3
RUN pip install flask
ADD practical1.py /
EXPOSE 5000 
CMD [ "python","./practical1.py" ]
