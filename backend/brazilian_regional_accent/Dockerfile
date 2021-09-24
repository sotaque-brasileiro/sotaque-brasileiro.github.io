FROM python:3.8-slim

# Install virtualenv and create a virtual environment
RUN pip install --no-cache-dir virtualenv==20.6.0 && virtualenv /env --python=python3.8
ENV PATH /env/bin:$PATH

# Removes output stream buffering, allowing for more efficient logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
WORKDIR /app
COPY requirements.txt .
RUN /env/bin/pip install --no-cache-dir -r requirements.txt

# Copy app, generate static and set permissions
COPY . .
RUN /env/bin/python manage.py collectstatic --no-input --settings=brazilian_regional_accent.settings.dev && \
  chown -R www-data:www-data /app

# Expose and run app
EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["/app/start-server.sh"]
