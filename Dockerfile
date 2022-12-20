FROM python:3

ADD bot_Zespuntéén_duizend.py /

RUN pip install pystrich

CMD [ "python", "./my_script.py" ]
