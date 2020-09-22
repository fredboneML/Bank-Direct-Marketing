FROM python:3.6

# Set the working directory.
WORKDIR /app

# copying all files over
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8501

# cmd to launch app when container is run
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]


