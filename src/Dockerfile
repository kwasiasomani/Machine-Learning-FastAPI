#Specifying which python image to pick up
FROM python:3.11

# Install dependencies
RUN pip install --no cache dir --upgrade pip

# set work diriectory
WORKDIR /app

# copy requirements.txt
COPY ./requirements.txt .

# Install requirements
RUN pip install --no cache dir -r requirements.txt

# copy project
COPY . .

# Expose the ports
EXPOSE 8086

# RUN the app when container launches
CMD ["API_app.py","--host", "0.0.0.0"]



