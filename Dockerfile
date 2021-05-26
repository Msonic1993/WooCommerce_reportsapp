FROM python:3.8
COPY ./reportsapp /reportsapp
COPY ./znowodronach_reports /znowodronach_reports
COPY ./manage.py /manage.py
COPY ./requirements.txt /requirements.txt
COPY ./start.sh /start.sh
RUN pip install -r /requirements.txt
RUN chmod +x /start.sh
CMD ["/start.sh"]
